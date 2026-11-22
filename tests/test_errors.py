"""Error mapping tests."""

from __future__ import annotations

import httpx2
import pytest

from aiosavorum import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    NotFoundError,
    PreconditionFailedError,
    PreconditionRequiredError,
    RateLimitError,
    SavorumError,
    ServerError,
    ValidationError,
)
from aiosavorum.errors import map_api_error


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        (401, AuthenticationError),
        (403, AuthorizationError),
        (404, NotFoundError),
        (409, ConflictError),
        (412, PreconditionFailedError),
        (422, ValidationError),
        (428, PreconditionRequiredError),
        (500, ServerError),
        (503, ServerError),
        (418, SavorumError),
    ],
)
def test_status_codes_map_to_public_errors(status: int, expected: type[SavorumError]) -> None:
    error = map_api_error(status, {"detail": "failure"})

    assert isinstance(error, expected)
    assert error.status_code == status
    assert error.message == "failure"


def test_rate_limit_error_reads_retry_after() -> None:
    response = httpx2.Response(429, headers={"retry-after": "12"})

    error = map_api_error(429, {"detail": "slow down"}, response=response)

    assert isinstance(error, RateLimitError)
    assert error.retry_after == 12.0


def test_conflict_error_reads_revision_from_body() -> None:
    error = map_api_error(412, {"detail": "stale", "params": {"revision": "8"}})

    assert isinstance(error, PreconditionFailedError)
    assert error.revision == 8


def test_conflict_error_reads_etag_when_body_has_no_revision() -> None:
    response = httpx2.Response(412, headers={"etag": 'W/"11"'})

    error = map_api_error(412, {"detail": "stale"}, response=response)

    assert isinstance(error, PreconditionFailedError)
    assert error.revision == 11


def test_error_code_uses_first_available_field() -> None:
    error = map_api_error(422, {"code": "invalid_title", "detail": "title is empty"})

    assert error.code == "invalid_title"


def test_unstructured_error_body_uses_status_message() -> None:
    error = map_api_error(500, 42)

    assert isinstance(error, ServerError)
    assert error.message == "Savorum API returned HTTP 500"


def test_conflict_error_reads_top_level_revision_with_params() -> None:
    body = {"detail": "stale", "params": {}, "revision": 8, "current_revision": 9}

    error = map_api_error(412, body)

    assert isinstance(error, PreconditionFailedError)
    assert error.revision == 8


def test_rate_limit_without_response_has_no_retry_after() -> None:
    error = map_api_error(429, {"detail": "slow down"})

    assert isinstance(error, RateLimitError)
    assert error.retry_after is None


def test_rate_limit_without_header_has_no_retry_after() -> None:
    response = httpx2.Response(429)

    error = map_api_error(429, {"detail": "slow down"}, response=response)

    assert isinstance(error, RateLimitError)
    assert error.retry_after is None


def test_rate_limit_ignores_invalid_retry_after() -> None:
    response = httpx2.Response(429, headers={"retry-after": "soon"})

    error = map_api_error(429, {"detail": "slow down"}, response=response)

    assert isinstance(error, RateLimitError)
    assert error.retry_after is None
