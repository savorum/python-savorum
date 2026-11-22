"""Async Python client for the Savorum HTTP API."""

from __future__ import annotations

from . import _generated as generated
from . import models
from .client import DEFAULT_BASE_URL, SavorumClient, if_match_for
from .errors import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    DeserializationError,
    NotFoundError,
    PreconditionFailedError,
    PreconditionRequiredError,
    RateLimitError,
    ResponseDecodeError,
    SavorumError,
    SavorumTimeoutError,
    ServerError,
    TransportError,
    ValidationError,
)
from .events import (
    ChangeEvent,
    CursorEvent,
    EventKind,
    ResyncEvent,
    StreamEvent,
)
from .pagination import Page

__version__ = "0.1.0"

__all__ = [
    "DEFAULT_BASE_URL",
    "AuthenticationError",
    "AuthorizationError",
    "ChangeEvent",
    "ConflictError",
    "CursorEvent",
    "DeserializationError",
    "EventKind",
    "NotFoundError",
    "Page",
    "PreconditionFailedError",
    "PreconditionRequiredError",
    "RateLimitError",
    "ResponseDecodeError",
    "ResyncEvent",
    "SavorumClient",
    "SavorumError",
    "SavorumTimeoutError",
    "ServerError",
    "StreamEvent",
    "TransportError",
    "ValidationError",
    "__version__",
    "generated",
    "if_match_for",
    "models",
]
