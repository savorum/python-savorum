"""Native HTTPX2 server-sent event support for ``/api/v1/events``."""

from __future__ import annotations

import asyncio
import json
import random
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Any

import httpx2

from ._transport import raise_response_error
from .errors import RateLimitError, ResponseDecodeError, ServerError, TransportError

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator, Mapping

__all__ = [
    "ChangeEvent",
    "CursorEvent",
    "EventKind",
    "ResyncEvent",
    "StreamEvent",
    "parse_event",
    "subscribe_events",
]


class EventKind(StrEnum):
    CHANGE = "change"
    RESYNC = "resync"
    CURSOR = "cursor"


@dataclass(frozen=True, slots=True)
class ChangeEvent:
    id: str
    occurred_at: datetime
    resource_type: str
    resource_id: str
    type: str
    version: int
    actor_id: str | None = None
    library_id: str | None = None
    correlation_id: str | None = None
    revision: int | None = None
    state: str | None = None
    list_id: str | None = None
    test: bool = False

    @property
    def kind(self) -> EventKind:
        return EventKind.CHANGE


@dataclass(frozen=True, slots=True)
class ResyncEvent:
    id: str
    reason: str

    @property
    def kind(self) -> EventKind:
        return EventKind.RESYNC


@dataclass(frozen=True, slots=True)
class CursorEvent:
    id: str

    @property
    def kind(self) -> EventKind:
        return EventKind.CURSOR


StreamEvent = ChangeEvent | ResyncEvent | CursorEvent


def _json_object(raw: httpx2.ServerSentEvent) -> dict[str, Any]:
    try:
        data = json.loads(raw.data)
    except ValueError as exc:
        message = "event data is not valid JSON"
        raise ResponseDecodeError(message) from exc
    if not isinstance(data, dict):
        message = "event data is not an object"
        raise ResponseDecodeError(message)
    return data


def _datetime(value: object) -> datetime:
    if not isinstance(value, str):
        message = "event occurred_at is missing"
        raise ResponseDecodeError(message)
    text = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(text)
    except ValueError as exc:
        message = "event occurred_at is invalid"
        raise ResponseDecodeError(message) from exc


def _optional_string(data: Mapping[str, Any], key: str) -> str | None:
    value = data.get(key)
    return value if isinstance(value, str) and value else None


def parse_event(raw: httpx2.ServerSentEvent) -> StreamEvent | None:
    """Decode one native HTTPX2 SSE frame.

    Unknown frame names return ``None`` so newer API versions can add facts
    without breaking existing consumers.
    """
    event_id = raw.id or ""
    name = raw.event or "message"

    if name == EventKind.CURSOR:
        return CursorEvent(id=event_id)
    if name == EventKind.RESYNC:
        data = _json_object(raw)
        reason = data.get("reason")
        return ResyncEvent(
            id=event_id,
            reason=reason if isinstance(reason, str) else "refresh-required",
        )
    if name != EventKind.CHANGE:
        return None

    data = _json_object(raw)
    resource = data.get("resource")
    payload = data.get("payload")
    resource = resource if isinstance(resource, dict) else {}
    payload = payload if isinstance(payload, dict) else {}

    try:
        version = int(data.get("version", 0))
    except (TypeError, ValueError, OverflowError) as exc:
        message = "event version is invalid"
        raise ResponseDecodeError(message) from exc

    revision = payload.get("revision")
    return ChangeEvent(
        id=_optional_string(data, "id") or event_id,
        occurred_at=_datetime(data.get("occurred_at")),
        resource_type=str(resource.get("type", "")),
        resource_id=str(resource.get("id", "")),
        type=str(data.get("type", "")),
        version=version,
        actor_id=_optional_string(data, "actor_id"),
        library_id=_optional_string(data, "library_id"),
        correlation_id=_optional_string(data, "correlation_id"),
        revision=revision if isinstance(revision, int) else None,
        state=_optional_string(payload, "state"),
        list_id=_optional_string(payload, "list_id"),
        test=payload.get("test") is True,
    )


async def subscribe_events(
    http_client: httpx2.AsyncClient,
    url: httpx2.URL | str,
    headers: Mapping[str, str],
    *,
    after: str | None = None,
    reconnect: bool = True,
    initial_backoff: float = 0.5,
    max_backoff: float = 30.0,
    jitter: float = 0.1,
) -> AsyncGenerator[StreamEvent, None]:
    """Yield decoded events from the Savorum stream.

    Resumes from ``after`` and then from the most recent SSE frame id. The
    server closes each stream after five minutes, so the subscription reconnects
    with exponential backoff until cancelled.
    """
    if initial_backoff <= 0 or max_backoff < initial_backoff:
        msg = "backoff bounds must satisfy 0 < initial_backoff <= max_backoff"
        raise ValueError(msg)

    cursor = after
    backoff = initial_backoff

    # An idle server sends a heartbeat every 15 seconds.
    timeout = httpx2.Timeout(http_client.timeout)
    if timeout.read is not None:
        timeout.read = max(timeout.read, 30.0)

    while True:
        connection_headers = dict(headers)
        connection_headers["Accept"] = "text/event-stream"
        if cursor:
            connection_headers["Last-Event-Id"] = cursor

        received = False
        try:
            async with http_client.sse(
                str(url), headers=connection_headers, timeout=timeout, follow_redirects=False
            ) as source:
                if source.response.has_redirect_location or source.response.status_code >= 400:
                    await source.response.aread()
                    raise_response_error(source.response)
                async for raw in source:
                    received = True
                    event = parse_event(raw)
                    if raw.id:
                        cursor = raw.id
                    if event is not None:
                        yield event
        except asyncio.CancelledError:
            raise
        except (RateLimitError, ServerError):
            if not reconnect:
                raise
        except httpx2.HTTPError as exc:
            if not reconnect:
                message = "event stream failed"
                raise TransportError(message) from exc
        else:
            if not reconnect:
                return
        if received:
            backoff = initial_backoff
        delay = backoff
        if jitter:
            delay += backoff * random.uniform(-jitter, jitter)  # noqa: S311
        await asyncio.sleep(max(0.0, delay))
        backoff = min(backoff * 2, max_backoff)
