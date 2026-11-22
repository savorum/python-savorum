"""Shared fixtures and payload builders for the mocked API tests."""

from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime

import httpx2
import pytest

from aiosavorum import models

RequestHandler = Callable[[httpx2.Request], httpx2.Response]

_CREATED_AT = datetime(2026, 1, 1, tzinfo=UTC)


def recipe_document() -> models.RecipeDocument:
    """Build the smallest valid SREF document the generated model accepts."""
    return models.RecipeDocument(
        id="recipe-1",
        ingredient_sections=[],
        instruction_sections=[],
        schema_version=1,
        title="Tea",
    )


def library_entry(*, revision: int = 3) -> models.LibraryEntry:
    """Build a revisioned library entry response."""
    return models.LibraryEntry(
        created_at=_CREATED_AT,
        id="recipe-1",
        recipe=recipe_document(),
        revision=revision,
        time_summary=models.TimeSummary(),
        updated_at=_CREATED_AT,
    )


def shopping_list() -> models.ShoppingList:
    """Build a shopping list response."""
    return models.ShoppingList(
        id="list-1",
        items=None,
        name="Groceries",
        requirements=models.ShoppingListRequirements(),
        revision=1,
        selections=models.ShoppingListSelections(),
    )


@pytest.fixture
def seen_requests() -> list[httpx2.Request]:
    return []


def capture(seen: list[httpx2.Request], response: httpx2.Response) -> RequestHandler:
    """Return a transport handler that records one request and replies once."""

    def handler(request: httpx2.Request) -> httpx2.Response:
        seen.append(request)
        return response

    return handler


def sequence(seen: list[httpx2.Request], responses: list[httpx2.Response]) -> RequestHandler:
    """Return a transport handler that replies from ``responses`` in order."""
    remaining = list(responses)

    def handler(request: httpx2.Request) -> httpx2.Response:
        seen.append(request)
        if not remaining:
            message = "unexpected request"
            raise AssertionError(message)
        return remaining.pop(0)

    return handler
