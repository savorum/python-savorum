"""SSE parsing and subscription tests."""

from __future__ import annotations

import asyncio
import json
from typing import TYPE_CHECKING

import httpx2
import pytest
from hypothesis import given
from hypothesis import strategies as st

from aiosavorum import (
    AuthenticationError,
    ChangeEvent,
    CursorEvent,
    EventKind,
    ResponseDecodeError,
    ResyncEvent,
    SavorumClient,
    ServerError,
    TransportError,
)
from aiosavorum.events import parse_event, subscribe_events

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

BASE_URL = "https://example.invalid"

CHANGE_DATA = {
    "id": "2",
    "occurred_at": "2026-01-01T00:00:00Z",
    "type": "recipe.updated",
    "version": 3,
    "resource": {"type": "recipe", "id": "recipe-1"},
    "payload": {"revision": 7, "state": "active", "list_id": "list-1", "test": False},
}


def sse_response(frames: str) -> httpx2.Response:
    return httpx2.Response(
        200,
        headers={"content-type": "text/event-stream"},
        content=frames.encode(),
    )


def test_change_event_parses_wire_shape() -> None:
    raw = httpx2.ServerSentEvent(event="change", id="2", data=json.dumps(CHANGE_DATA))

    event = parse_event(raw)

    assert isinstance(event, ChangeEvent)
    assert event.kind == EventKind.CHANGE
    assert event.id == "2"
    assert event.resource_type == "recipe"
    assert event.resource_id == "recipe-1"
    assert event.type == "recipe.updated"
    assert event.version == 3
    assert event.revision == 7
    assert event.state == "active"
    assert event.list_id == "list-1"
    assert event.occurred_at.year == 2026


def test_resync_and_cursor_events_parse() -> None:
    resync = parse_event(
        httpx2.ServerSentEvent(
            event="resync",
            id="3",
            data=json.dumps({"reason": "refresh-required"}),
        )
    )
    cursor = parse_event(httpx2.ServerSentEvent(event="cursor", id="1", data="{}"))

    assert isinstance(resync, ResyncEvent)
    assert resync.kind == EventKind.RESYNC
    assert resync.reason == "refresh-required"
    assert isinstance(cursor, CursorEvent)
    assert cursor.kind == EventKind.CURSOR
    assert cursor.id == "1"


def test_unknown_event_is_ignored() -> None:
    assert parse_event(httpx2.ServerSentEvent(event="future", id="4", data="{}")) is None


async def test_subscription_reconnects_with_last_event_id() -> None:
    first = (
        "event: cursor\nid: 1\ndata: {}\n\n"
        f"event: change\nid: 2\ndata: {json.dumps(CHANGE_DATA)}\n\n"
    )
    second = 'event: resync\nid: 3\ndata: {"reason":"refresh-required"}\n\n'
    requests: list[httpx2.Request] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        requests.append(request)
        if len(requests) == 1:
            return sse_response(first)
        return sse_response(second)

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handler)) as http:
        client = SavorumClient(
            base_url=BASE_URL,
            token="token-1",
            library_id="library-1",
            client=http,
        )
        subscription = client.events(
            after="seed",
            initial_backoff=0.001,
            max_backoff=0.001,
            jitter=0.0,
        )
        received = []
        async for event in subscription:
            received.append(event)
            if len(received) == 3:
                break
        await subscription.aclose()

    assert [event.kind for event in received] == [
        EventKind.CURSOR,
        EventKind.CHANGE,
        EventKind.RESYNC,
    ]
    assert len(requests) == 2
    assert str(requests[0].url) == f"{BASE_URL}/api/v1/events"
    assert requests[0].headers["last-event-id"] == "seed"
    assert requests[1].headers["last-event-id"] == "2"
    for request in requests:
        assert request.headers["accept"] == "text/event-stream"
        assert request.headers["authorization"] == "Bearer token-1"
        assert request.headers["x-savorum-library"] == "library-1"


async def test_non_retriable_event_error_propagates() -> None:
    async def body() -> AsyncIterator[bytes]:
        yield b'{"detail":"unauthorized","status":401}'

    response = httpx2.Response(401, content=body())

    async with httpx2.AsyncClient(
        transport=httpx2.MockTransport(lambda _request: response)
    ) as http:
        client = SavorumClient(base_url=BASE_URL, client=http)
        subscription = client.events()

        with pytest.raises(AuthenticationError):
            await anext(subscription)
        await subscription.aclose()


async def test_transport_error_reconnects_without_losing_events() -> None:
    requests: list[httpx2.Request] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        requests.append(request)
        if len(requests) == 1:
            message = "connection reset"
            raise httpx2.ConnectError(message)
        return sse_response("event: cursor\nid: 9\ndata: {}\n\n")

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handler)) as http:
        client = SavorumClient(base_url=BASE_URL, client=http)
        subscription = client.events(
            initial_backoff=0.001,
            max_backoff=0.001,
            jitter=0.1,
        )
        event = await anext(subscription)
        await subscription.aclose()

    assert isinstance(event, CursorEvent)
    assert event.id == "9"
    assert len(requests) == 2


def test_malformed_event_data_is_rejected() -> None:
    with pytest.raises(ResponseDecodeError):
        parse_event(httpx2.ServerSentEvent(event="change", id="1", data="not json"))
    with pytest.raises(ResponseDecodeError):
        parse_event(httpx2.ServerSentEvent(event="change", id="1", data="[]"))


def test_invalid_change_timestamp_is_rejected() -> None:
    invalid_type = dict(CHANGE_DATA, occurred_at=123)
    invalid_value = dict(CHANGE_DATA, occurred_at="not-a-date")

    with pytest.raises(ResponseDecodeError, match="missing"):
        parse_event(httpx2.ServerSentEvent(event="change", id="1", data=json.dumps(invalid_type)))
    with pytest.raises(ResponseDecodeError, match="invalid"):
        parse_event(httpx2.ServerSentEvent(event="change", id="1", data=json.dumps(invalid_value)))


async def test_invalid_backoff_bounds_are_rejected() -> None:
    async with httpx2.AsyncClient() as http:
        client = SavorumClient(base_url=BASE_URL, client=http)
        subscription = client.events(initial_backoff=0)

        with pytest.raises(ValueError, match="backoff bounds"):
            await anext(subscription)
        await subscription.aclose()


async def test_cancellation_is_not_swallowed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def cancelled_sse(
        _self: httpx2.AsyncClient,
        *_args: object,
        **_kwargs: object,
    ) -> None:
        raise asyncio.CancelledError

    monkeypatch.setattr(httpx2.AsyncClient, "sse", cancelled_sse)

    async with httpx2.AsyncClient() as http:
        subscription = subscribe_events(http, BASE_URL, {})

        with pytest.raises(asyncio.CancelledError):
            await anext(subscription)
        await subscription.aclose()


async def test_retriable_error_propagates_when_reconnect_disabled() -> None:
    response = httpx2.Response(500, json={"detail": "server failed"})

    async with httpx2.AsyncClient(
        transport=httpx2.MockTransport(lambda _request: response)
    ) as http:
        client = SavorumClient(base_url=BASE_URL, client=http)
        subscription = client.events(reconnect=False)

        with pytest.raises(ServerError):
            await anext(subscription)
        await subscription.aclose()


async def test_http_error_becomes_transport_error_when_reconnect_disabled() -> None:
    def handler(_request: httpx2.Request) -> httpx2.Response:
        message = "connection reset"
        raise httpx2.ConnectError(message)

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handler)) as http:
        client = SavorumClient(base_url=BASE_URL, client=http)
        subscription = client.events(reconnect=False)

        with pytest.raises(TransportError):
            await anext(subscription)
        await subscription.aclose()


async def test_closed_stream_returns_without_reconnect() -> None:
    stream = sse_response("event: cursor\nid: 1\ndata: {}\n\n")

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(lambda _request: stream)) as http:
        client = SavorumClient(base_url=BASE_URL, client=http)

        events = [event async for event in client.events(reconnect=False)]

    assert [event.id for event in events] == ["1"]


async def test_streamed_service_error_reconnects() -> None:
    async def body() -> AsyncIterator[bytes]:
        yield b'{"detail":"unavailable"}'

    responses = iter(
        [httpx2.Response(503, content=body()), sse_response("event: cursor\nid: 8\ndata: {}\n\n")]
    )

    def handler(request: httpx2.Request) -> httpx2.Response:
        assert request.extensions["timeout"]["read"] >= 30
        return next(responses)

    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handler)) as http:
        subscription = SavorumClient(client=http).events(initial_backoff=0.001)
        assert (await anext(subscription)).id == "8"
        await subscription.aclose()


@given(st.one_of(st.none(), st.dictionaries(st.text(), st.integers()), st.lists(st.integers())))
def test_invalid_json_version_has_a_typed_error(version: object) -> None:
    raw = httpx2.ServerSentEvent(
        event="change", data=json.dumps(dict(CHANGE_DATA, version=version))
    )
    with pytest.raises(ResponseDecodeError, match="version"):
        parse_event(raw)
