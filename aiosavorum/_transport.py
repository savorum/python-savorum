"""HTTP execution shared by the public client and the generated endpoint modules."""

from __future__ import annotations

import importlib
import re
from collections.abc import Callable, Mapping
from typing import Any, Protocol, cast

import httpx2

from . import _generated
from ._generated.errors import UnexpectedStatus as GeneratedUnexpectedStatus
from .errors import (
    DeserializationError,
    SavorumTimeoutError,
    TransportError,
    map_api_error,
)

_NAME_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")


class _EndpointModule(Protocol):
    def _get_kwargs(self, **kwargs: Any) -> dict[str, Any]: ...

    def _build_response(
        self,
        *,
        client: _generated.Client,
        response: httpx2.Response,
    ) -> Any: ...


EndpointCallable = Callable[..., Any]


def _merge_headers(base: Mapping[str, str], extra: object) -> dict[str, str]:
    headers = dict(base)
    if isinstance(extra, Mapping):
        headers.update({str(key): str(value) for key, value in extra.items()})
    return headers


def _json_object(response: httpx2.Response) -> dict[str, Any]:
    try:
        data = response.json()
    except ValueError:
        return {}
    return data if isinstance(data, dict) else {}


class _RequestExecutor:
    def __init__(
        self,
        *,
        base_url: str,
        headers: Mapping[str, str],
        http_client: httpx2.AsyncClient,
    ) -> None:
        self.base_url = base_url
        self.headers = dict(headers)
        self.http_client = http_client
        self._generated_client = _generated.Client(
            base_url=base_url,
            raise_on_unexpected_status=True,
        )

    def _url(self, path: str) -> httpx2.URL:
        return httpx2.URL(self.base_url.rstrip("/") + "/" + path.lstrip("/"))

    def url(self, path: str) -> httpx2.URL:
        """Resolve an API path against the configured base URL."""
        return self._url(path)

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: object = None,
        json: object = None,
        content: object = None,
        headers: Mapping[str, str] | None = None,
        request_timeout: float | httpx2.Timeout | None = None,
    ) -> httpx2.Response:
        request_headers = _merge_headers(self.headers, headers)
        kwargs: dict[str, Any] = {
            "method": method,
            "url": self._url(path),
            "headers": request_headers,
        }
        if params is not None:
            kwargs["params"] = params
        if json is not None:
            kwargs["json"] = json
        if content is not None:
            kwargs["content"] = content
        if request_timeout is not None:
            kwargs["timeout"] = request_timeout

        try:
            response = await self.http_client.request(**kwargs, follow_redirects=False)
        except httpx2.TimeoutException as exc:
            message = "request timed out"
            raise SavorumTimeoutError(message) from exc
        except httpx2.RequestError as exc:
            message = "request failed"
            raise TransportError(message) from exc
        return response

    async def call_endpoint(
        self,
        module: _EndpointModule,
        **kwargs: Any,
    ) -> Any:
        request = module._get_kwargs(**kwargs)
        request_headers = _merge_headers(self.headers, request.pop("headers", None))
        request["headers"] = request_headers
        request["url"] = self._url(request["url"])

        try:
            response = await self.http_client.request(**request, follow_redirects=False)
        except httpx2.TimeoutException as exc:
            message = "request timed out"
            raise SavorumTimeoutError(message) from exc
        except httpx2.RequestError as exc:
            message = "request failed"
            raise TransportError(message) from exc

        if response.has_redirect_location:
            raise_response_error(response)

        if response.status_code >= 400:
            parsed: object = None
            try:
                parsed = module._build_response(
                    client=self._generated_client,
                    response=response,
                ).parsed
            except GeneratedUnexpectedStatus:
                parsed = _json_object(response)
            except (LookupError, TypeError, ValueError, AttributeError):
                parsed = _json_object(response)
            raise map_api_error(response.status_code, parsed, response=response)

        try:
            built = module._build_response(
                client=self._generated_client,
                response=response,
            )
        except GeneratedUnexpectedStatus as exc:
            raise map_api_error(exc.status_code, _json_object(response), response=response) from exc
        except (LookupError, TypeError, ValueError, AttributeError) as exc:
            message = "response decode failed"
            raise DeserializationError(
                message,
                status_code=response.status_code,
                response=response,
            ) from exc
        return built.parsed


class _TagProxy:
    def __init__(self, executor: _RequestExecutor, tag: str) -> None:
        self._executor = executor
        self._tag = tag

    def __getattr__(self, name: str) -> EndpointCallable:
        if name.startswith("_") or not _NAME_PATTERN.fullmatch(name):
            raise AttributeError(name)
        try:
            module = importlib.import_module(f"{_generated.__name__}.api.{self._tag}.{name}")
        except ModuleNotFoundError as exc:
            raise AttributeError(name) from exc
        endpoint = cast("_EndpointModule", module)
        if not hasattr(endpoint, "_get_kwargs") or not hasattr(endpoint, "_build_response"):
            raise AttributeError(name)

        async def call(**kwargs: Any) -> Any:
            return await self._executor.call_endpoint(endpoint, **kwargs)

        call.__name__ = f"{self._tag}_{name}"
        return call


class ApiProxy:
    """Access every generated endpoint with the client's credentials applied.

    ``client.api.recipes.list_recipes(limit=10)`` resolves to the generated
    ``api/recipes/list_recipes`` module. Arguments match the generated endpoint
    function; the return value is its parsed model.
    """

    def __init__(self, executor: _RequestExecutor) -> None:
        self._executor = executor

    def __getattr__(self, tag: str) -> _TagProxy:
        if tag.startswith("_") or not _NAME_PATTERN.fullmatch(tag):
            raise AttributeError(tag)
        return _TagProxy(self._executor, tag)


def raise_response_error(response: httpx2.Response) -> None:
    """Raise a public exception when a raw response has an error status."""
    if response.status_code < 400 and not response.has_redirect_location:
        return
    raise map_api_error(response.status_code, _json_object(response), response=response)


__all__ = ["ApiProxy", "EndpointCallable", "raise_response_error"]
