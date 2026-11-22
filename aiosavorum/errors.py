"""Exceptions raised by :mod:`aiosavorum`."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import httpx2

__all__ = [
    "AuthenticationError",
    "AuthorizationError",
    "ConflictError",
    "DeserializationError",
    "NotFoundError",
    "PreconditionFailedError",
    "PreconditionRequiredError",
    "RateLimitError",
    "ResponseDecodeError",
    "SavorumError",
    "SavorumTimeoutError",
    "ServerError",
    "TransportError",
    "ValidationError",
]


class SavorumError(Exception):
    """Base class for errors raised by the client."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        code: str | None = None,
        response: httpx2.Response | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.code = code
        self.response = response


class TransportError(SavorumError):
    """The request could not be completed."""


class SavorumTimeoutError(SavorumError):
    """The request exceeded its timeout."""


class ResponseDecodeError(SavorumError):
    """The server returned a body the generated models could not parse."""


class DeserializationError(ResponseDecodeError):
    """A successful response body could not be converted to a model."""


class AuthenticationError(SavorumError):
    """The request lacks valid credentials (HTTP 401)."""


class AuthorizationError(SavorumError):
    """The credentials do not grant access (HTTP 403)."""


class NotFoundError(SavorumError):
    """The resource does not exist (HTTP 404)."""


class ConflictError(SavorumError):
    """The write conflicts with the current resource revision (HTTP 409)."""

    def __init__(self, *args: Any, revision: int | None = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.revision = revision


class PreconditionFailedError(ConflictError):
    """If-Match did not match the current revision (HTTP 412)."""


class PreconditionRequiredError(SavorumError):
    """A write requires If-Match (HTTP 428)."""


class ValidationError(SavorumError):
    """The server rejected the request body or parameters (HTTP 422)."""


class RateLimitError(SavorumError):
    """The server rate-limited the request (HTTP 429)."""

    def __init__(
        self,
        *args: Any,
        retry_after: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.retry_after = retry_after


class ServerError(SavorumError):
    """The server failed to complete the request (HTTP 500 or 503)."""


def _body_as_mapping(value: object) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return {str(key): item for key, item in value.items()}
    to_dict = getattr(value, "to_dict", None)
    if callable(to_dict):
        result = to_dict()
        if isinstance(result, Mapping):
            return {str(key): item for key, item in result.items()}
    return {}


def _first_string(body: dict[str, Any], names: tuple[str, ...]) -> str | None:
    for name in names:
        value = body.get(name)
        if isinstance(value, str) and value:
            return value
    return None


def _response_message(body: dict[str, Any], status_code: int) -> str:
    message = _first_string(body, ("detail", "message", "title", "error", "code"))
    return message or f"Savorum API returned HTTP {status_code}"


def _revision_from(body: dict[str, Any], response: httpx2.Response | None) -> int | None:
    candidates: list[object] = []
    params = body.get("params")
    if isinstance(params, Mapping):
        for key in ("revision", "current_revision", "expected_revision"):
            if key in params:
                candidates.append(params[key])
            if key in body:
                candidates.append(body[key])
    for candidate in candidates:
        if isinstance(candidate, int):
            return candidate
        if isinstance(candidate, str) and candidate.isdigit():
            return int(candidate)

    if response is not None:
        etag = response.headers.get("etag", "")
        match = re.search(r'(?:W/)?"?(\d+)"?', etag)
        if match is not None:
            return int(match.group(1))
    return None


def _retry_after(response: httpx2.Response | None) -> float | None:
    if response is None:
        return None
    value = response.headers.get("retry-after")
    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def map_api_error(
    status_code: int,
    parsed: object,
    *,
    response: httpx2.Response | None = None,
) -> SavorumError:
    """Convert a documented error response into the matching exception."""
    body = _body_as_mapping(parsed)
    message = _response_message(body, status_code)
    code = _first_string(body, ("code", "error"))
    common: dict[str, Any] = {
        "status_code": status_code,
        "code": code,
        "response": response,
    }

    if status_code in (401, 407):
        return AuthenticationError(message, **common)
    if status_code == 403:
        return AuthorizationError(message, **common)
    if status_code == 404:
        return NotFoundError(message, **common)
    if status_code in (409, 412):
        error_class = ConflictError if status_code == 409 else PreconditionFailedError
        return error_class(
            message,
            revision=_revision_from(body, response),
            **common,
        )
    if status_code == 428:
        return PreconditionRequiredError(message, **common)
    if status_code == 422:
        return ValidationError(message, **common)
    if status_code == 429:
        return RateLimitError(message, retry_after=_retry_after(response), **common)
    if status_code >= 500:
        return ServerError(message, **common)
    return SavorumError(message, **common)
