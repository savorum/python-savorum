"""Transport edge cases for the hand-written execution layer."""

from __future__ import annotations

import httpx2
import pytest

from aiosavorum import (
    SavorumClient,
    SavorumError,
    SavorumTimeoutError,
    ServerError,
    TransportError,
)
from tests.conftest import capture, sequence

BASE_URL = "https://example.invalid"


def make_client(handler: object, **kwargs: object) -> SavorumClient:
    transport = httpx2.MockTransport(handler)  # type: ignore[arg-type]
    http_client = httpx2.AsyncClient(transport=transport)
    return SavorumClient(base_url=BASE_URL, client=http_client, **kwargs)  # type: ignore[arg-type]


async def test_invalid_error_body_falls_back_to_empty_object() -> None:
    response = httpx2.Response(400, content=b"not json")
    client = make_client(lambda _request: response)

    with pytest.raises(SavorumError) as exc_info:
        await client.request("GET", "/api/v1/raw")

    assert exc_info.value.status_code == 400
    assert exc_info.value.code is None
    await client.aclose()


async def test_raw_request_sends_json_content_and_timeout(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(200, json={"ok": True})
    client = make_client(sequence(seen_requests, [response, response]))

    await client.request("POST", "/api/v1/raw", json={"name": "tea"}, request_timeout=5.0)
    await client.request("POST", "/api/v1/raw", content=b"payload")

    assert seen_requests[0].headers["content-type"] == "application/json"
    assert seen_requests[1].content == b"payload"
    await client.aclose()


async def test_raw_request_wraps_timeout_and_transport_errors() -> None:
    def timeout(_request: httpx2.Request) -> httpx2.Response:
        message = "timed out"
        raise httpx2.ReadTimeout(message)

    client = make_client(timeout)
    with pytest.raises(SavorumTimeoutError):
        await client.request("GET", "/api/v1/raw")
    await client.aclose()

    def disconnect(_request: httpx2.Request) -> httpx2.Response:
        message = "connection reset"
        raise httpx2.ConnectError(message)

    client = make_client(disconnect)
    with pytest.raises(TransportError):
        await client.request("GET", "/api/v1/raw")
    await client.aclose()


async def test_generated_call_wraps_transport_error() -> None:
    def disconnect(_request: httpx2.Request) -> httpx2.Response:
        message = "connection reset"
        raise httpx2.ConnectError(message)

    client = make_client(disconnect)

    with pytest.raises(TransportError):
        await client.get_health()

    await client.aclose()


async def test_generated_call_maps_unexpected_error_status() -> None:
    response = httpx2.Response(418, json={"detail": "teapot"})
    client = make_client(capture([], response))

    with pytest.raises(SavorumError) as exc_info:
        await client.get_health()

    assert exc_info.value.status_code == 418
    assert "teapot" in str(exc_info.value)
    await client.aclose()


async def test_generated_call_maps_malformed_error_body() -> None:
    response = httpx2.Response(500, content=b"not json")
    client = make_client(capture([], response))

    with pytest.raises(ServerError):
        await client.get_health()

    await client.aclose()


async def test_generated_call_maps_undocumented_success_status() -> None:
    response = httpx2.Response(204)
    client = make_client(capture([], response))

    with pytest.raises(SavorumError) as exc_info:
        await client.get_health()

    assert exc_info.value.status_code == 204
    await client.aclose()


async def test_proxy_rejects_invalid_names(monkeypatch: pytest.MonkeyPatch) -> None:
    client = make_client(lambda _request: httpx2.Response(200, json={"status": "ok"}))

    with pytest.raises(AttributeError):
        _ = client.api._private
    with pytest.raises(AttributeError):
        _ = client.api.recipes._private
    with pytest.raises(AttributeError):
        _ = client.api.recipes.no_such_endpoint

    monkeypatch.setattr("aiosavorum._transport.importlib.import_module", lambda _name: object())
    with pytest.raises(AttributeError):
        _ = client.api.recipes.get_recipe

    await client.aclose()


@pytest.mark.parametrize("operation", ["raw", "typed", "stream"])
async def test_instance_redirect_is_reported_to_caller(operation: str) -> None:
    requests: list[httpx2.Request] = []
    response = httpx2.Response(307, headers={"Location": "https://other.invalid/"})
    transport = httpx2.MockTransport(sequence(requests, [response]))
    async with httpx2.AsyncClient(transport=transport, follow_redirects=True) as http:
        client = SavorumClient(base_url=BASE_URL, client=http, library_id="library")
        with pytest.raises(SavorumError) as error:
            if operation == "raw":
                await client.request("POST", "/write", json={"value": 1})
            elif operation == "typed":
                await client.get_health()
            else:
                await anext(client.events())
        assert error.value.status_code == 307
        assert len(requests) == 1
        assert http.follow_redirects
