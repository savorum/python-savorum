"""Mocked transport tests for the ergonomic client."""

from __future__ import annotations

from datetime import UTC, datetime

import httpx2
import pytest

from aiosavorum import (
    DEFAULT_BASE_URL,
    AuthenticationError,
    DeserializationError,
    NotFoundError,
    Page,
    PreconditionFailedError,
    ResponseDecodeError,
    SavorumClient,
    SavorumTimeoutError,
    if_match_for,
    models,
)
from aiosavorum.client import _page, _require
from tests.conftest import (
    capture,
    library_entry,
    recipe_document,
    sequence,
    shopping_list,
)

BASE_URL = "https://example.invalid/savorum"


def make_client(handler: object, **kwargs: object) -> SavorumClient:
    transport = httpx2.MockTransport(handler)  # type: ignore[arg-type]
    http_client = httpx2.AsyncClient(transport=transport)
    return SavorumClient(base_url=BASE_URL, client=http_client, **kwargs)  # type: ignore[arg-type]


async def test_injected_client_is_not_closed_and_credentials_are_per_request(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(200, json={"status": "ok"})
    async with httpx2.AsyncClient(
        transport=httpx2.MockTransport(capture(seen_requests, response))
    ) as http:
        async with SavorumClient(
            base_url=BASE_URL,
            token="token-1",
            library_id="library-1",
            client=http,
        ) as client:
            assert client.base_url == BASE_URL
            assert client.owns_client is False
            health = await client.get_health()
            assert health is not None
            assert str(health.status) == "ok"
            await client.aclose()
            assert http.is_closed is False

        await http.get("/still-open")

    request = seen_requests[0]
    assert str(request.url) == f"{BASE_URL}/api/v1/health"
    assert request.headers["authorization"] == "Bearer token-1"
    assert request.headers["x-savorum-library"] == "library-1"
    assert request.headers["accept"] == "application/json"
    assert request.headers["user-agent"].startswith("aiosavorum/")
    assert len(seen_requests) == 2


async def test_cloud_url_with_trailing_slash_is_normalized(
    seen_requests: list[httpx2.Request],
) -> None:
    cloud_url = "https://example.my.savorum.net/"
    response = httpx2.Response(200, json={"status": "ok"})
    async with httpx2.AsyncClient(
        transport=httpx2.MockTransport(capture(seen_requests, response))
    ) as http:
        client = SavorumClient(base_url=cloud_url, client=http)

        await client.get_health()

    assert client.base_url == cloud_url.rstrip("/")
    assert str(seen_requests[0].url) == f"{cloud_url}api/v1/health"


async def test_internal_client_is_owned_and_closed() -> None:
    client = SavorumClient(base_url=DEFAULT_BASE_URL)
    assert client.owns_client is True
    await client.aclose()
    assert client._http_client.is_closed is True

    await client.aclose()


async def test_for_library_shares_client_and_overrides_library_header(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(200, json={"status": "ok"})
    async with httpx2.AsyncClient(
        transport=httpx2.MockTransport(capture(seen_requests, response))
    ) as http:
        client = SavorumClient(
            base_url=BASE_URL,
            token="token-1",
            library_id="library-1",
            client=http,
        )
        scoped = client.for_library("library-2")

        await scoped.get_health()

        assert scoped._http_client is http
        assert scoped.owns_client is False
        assert seen_requests[0].headers["authorization"] == "Bearer token-1"
        assert seen_requests[0].headers["x-savorum-library"] == "library-2"


async def test_generated_proxy_executes_on_injected_client(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(200, json={"status": "ok"})
    client = make_client(capture(seen_requests, response))

    health = await client.api.instance.get_health()

    assert health is not None
    assert str(health.status) == "ok"
    assert seen_requests[0].url.path == "/savorum/api/v1/health"
    await client.aclose()


async def test_list_recipes_page_builds_query_and_page(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(
        200,
        json=models.ListRecipesOutputBody(items=[], limit=2, offset=2, total=5).to_dict(),
    )
    client = make_client(capture(seen_requests, response))

    page = await client.list_recipes_page(q="tea", limit=2, offset=2)

    assert page.items == ()
    assert (page.offset, page.limit, page.total, page.has_next) == (2, 2, 5, True)
    assert seen_requests[0].url.params["q"] == "tea"
    assert seen_requests[0].url.params["limit"] == "2"
    assert seen_requests[0].url.params["offset"] == "2"
    await client.aclose()


async def test_revisions_page_without_total_is_supported(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(
        200,
        json=models.ListRevisionsOutputBody(items=[], limit=50, offset=0).to_dict(),
    )
    client = make_client(capture(seen_requests, response))

    page = await client.list_recipe_revisions_page("recipe-1")

    assert page.items == ()
    assert page.total is None
    assert page.has_next is False
    await client.aclose()


async def test_conditional_write_sends_if_match_header(
    seen_requests: list[httpx2.Request],
) -> None:
    entry = library_entry(revision=3)
    response = httpx2.Response(200, json=entry.to_dict())
    client = make_client(capture(seen_requests, response))

    result = await client.trash_recipe("recipe-1", if_match=if_match_for(entry))

    assert result.revision == 3
    assert seen_requests[0].headers["if-match"] == '"3"'
    assert seen_requests[0].method == "DELETE"
    await client.aclose()


async def test_create_recipe_sends_idempotency_key(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(201, json=library_entry().to_dict())
    client = make_client(capture(seen_requests, response))

    result = await client.create_recipe(recipe_document(), idempotency_key="import-42")

    assert result.id == "recipe-1"
    assert seen_requests[0].headers["idempotency-key"] == "import-42"
    assert seen_requests[0].headers["content-type"] == "application/json"
    await client.aclose()


async def test_get_groceries_requires_list_id(seen_requests: list[httpx2.Request]) -> None:
    response = httpx2.Response(200, json=shopping_list().to_dict())
    client = make_client(capture(seen_requests, response))

    result = await client.get_groceries("list-1")

    assert result.name == "Groceries"
    assert seen_requests[0].url.path == "/savorum/api/v1/shopping/lists/list-1"
    await client.aclose()


async def test_api_error_is_mapped(seen_requests: list[httpx2.Request]) -> None:
    response = httpx2.Response(
        404,
        json={"detail": "recipe missing", "code": "not_found", "status": 404},
    )
    client = make_client(capture(seen_requests, response))

    with pytest.raises(NotFoundError) as exc_info:
        await client.get_recipe("missing")

    assert exc_info.value.status_code == 404
    assert exc_info.value.code == "not_found"
    assert "recipe missing" in str(exc_info.value)
    await client.aclose()


async def test_precondition_error_reports_revision(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(
        412,
        json={"detail": "stale revision", "params": {"revision": 9}},
        headers={"etag": '"10"'},
    )
    client = make_client(capture(seen_requests, response))

    with pytest.raises(PreconditionFailedError) as exc_info:
        await client.request("DELETE", "/api/v1/recipes/recipe-1")

    assert exc_info.value.revision == 9
    await client.aclose()


async def test_deserialization_failure_is_wrapped(seen_requests: list[httpx2.Request]) -> None:
    response = httpx2.Response(200, json={"status": "unexpected"})
    client = make_client(capture(seen_requests, response))

    with pytest.raises(DeserializationError):
        await client.get_health()

    await client.aclose()


async def test_timeout_is_wrapped() -> None:
    def handler(_request: httpx2.Request) -> httpx2.Response:
        message = "timed out"
        raise httpx2.ReadTimeout(message)

    client = make_client(handler)

    with pytest.raises(SavorumTimeoutError):
        await client.get_health()

    await client.aclose()


async def test_raw_request_can_suppress_status_errors(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(401, json={"detail": "unauthorized", "status": 401})
    client = make_client(capture(seen_requests, response))

    raw = await client.request("GET", "/api/v1/raw", raise_for_status=False)
    assert raw.status_code == 401

    with pytest.raises(AuthenticationError):
        await client.request("GET", "/api/v1/raw")

    assert len(seen_requests) == 2
    await client.aclose()


async def test_raw_request_merges_headers_without_mutating_client(
    seen_requests: list[httpx2.Request],
) -> None:
    response = httpx2.Response(200, json={"ok": True})
    client = make_client(capture(seen_requests, response), token="token-1")

    response = await client.request(
        "GET",
        "/api/v1/raw",
        headers={"X-Extra": "value"},
        params={"limit": 1},
    )

    assert response.status_code == 200
    assert seen_requests[0].headers["authorization"] == "Bearer token-1"
    assert seen_requests[0].headers["x-extra"] == "value"
    assert seen_requests[0].url.params["limit"] == "1"
    await client.aclose()


async def test_error_sequence_helper_supports_multiple_responses(
    seen_requests: list[httpx2.Request],
) -> None:
    responses = [
        httpx2.Response(200, json={"status": "ok"}),
        httpx2.Response(200, json={"status": "ok"}),
    ]
    client = make_client(sequence(seen_requests, responses))

    assert await client.get_health() is not None
    assert await client.get_health() is not None
    assert len(seen_requests) == 2
    await client.aclose()


def test_internal_helpers_handle_missing_data() -> None:
    with pytest.raises(ResponseDecodeError, match="empty"):
        _require(None, "empty response")

    page: Page[object] = _page(None, offset=4, limit=10)

    assert (page.items, page.offset, page.limit, page.total, page.has_next) == (
        (),
        4,
        10,
        4,
        False,
    )


async def test_read_wrappers_return_generated_models(
    seen_requests: list[httpx2.Request],
) -> None:
    timestamp = datetime(2026, 1, 1, tzinfo=UTC).isoformat().replace("+00:00", "Z")
    responses = [
        httpx2.Response(
            200,
            json={
                "api_major": 1,
                "auth_enabled": True,
                "auth_methods": [],
                "links": {
                    "guide": "https://example.invalid/guide",
                    "openapi": "https://example.invalid/openapi.json",
                    "tokens": "https://example.invalid/tokens",
                },
                "product": "Savorum",
                "schema_version": 1,
                "version": "1",
            },
        ),
        httpx2.Response(
            200,
            json={
                "active_library_id": "library-1",
                "auth_enabled": True,
                "csrf_token": "csrf",
                "libraries": [{"id": "library-1", "name": "Kitchen", "role": "owner"}],
                "passkeys_available": False,
                "recovery_authenticated": False,
                "user": None,
            },
        ),
        httpx2.Response(
            200,
            json={
                "policy": {
                    "allow_nonexpiring": False,
                    "default_days": 30,
                    "maximum_days": 365,
                },
                "tokens": [],
            },
        ),
        httpx2.Response(200, json={"libraries": []}),
        httpx2.Response(200, json=library_entry().to_dict()),
        httpx2.Response(
            200,
            json={
                "created_at": timestamp,
                "entries": [],
                "id": "book-1",
                "kind": "personal",
                "revision": 1,
                "sections": [],
                "title": "Favorites",
                "updated_at": timestamp,
            },
        ),
        httpx2.Response(200, json=[{"id": "list-1", "name": "Groceries"}]),
        httpx2.Response(
            200,
            json={
                "cause": "api",
                "created_at": timestamp,
                "library_entry_id": "recipe-1",
                "recipe": recipe_document().to_dict(),
                "revision": 2,
                "state": "active",
            },
        ),
    ]
    client = make_client(sequence(seen_requests, responses))

    capabilities = await client.get_capabilities()
    account = await client.get_current_account()
    tokens = await client.list_account_tokens()
    libraries = await client.list_libraries()
    recipe = await client.get_recipe("recipe-1")
    book = await client.get_book("book-1")
    shopping_lists = await client.list_shopping_lists()
    revision = await client.get_recipe_revision("recipe-1", 2)

    assert capabilities.product == "Savorum"
    assert account.active_library_id == "library-1"
    assert tokens.tokens == []
    assert libraries == []
    assert recipe is not None and recipe.id == "recipe-1"
    assert book is not None and book.id == "book-1"
    assert [item.name for item in shopping_lists] == ["Groceries"]
    assert revision.revision == 2
    assert len(seen_requests) == 8
    await client.aclose()


async def test_write_wrappers_accept_optional_preconditions(
    seen_requests: list[httpx2.Request],
) -> None:
    responses = [
        httpx2.Response(200, json=library_entry(revision=4).to_dict()),
        httpx2.Response(200, json=library_entry(revision=5).to_dict()),
        httpx2.Response(201, json=shopping_list().to_dict()),
    ]
    client = make_client(sequence(seen_requests, responses))

    replaced = await client.replace_recipe("recipe-1", recipe_document(), if_match=3)
    restored = await client.restore_recipe("recipe-1")
    created = await client.create_shopping_list(
        models.ShoppingListInput(id="list-2", name="Errands")
    )

    assert replaced.revision == 4
    assert seen_requests[0].headers["if-match"] == '"3"'
    assert restored.revision == 5
    assert "if-match" not in seen_requests[1].headers
    assert created.name == "Groceries"
    assert len(seen_requests) == 3
    await client.aclose()


async def test_collection_iterators_use_page_helpers(
    seen_requests: list[httpx2.Request],
) -> None:
    responses = [
        httpx2.Response(
            200,
            json=models.ListRecipesOutputBody(items=[], limit=2, offset=0, total=0).to_dict(),
        ),
        httpx2.Response(
            200,
            json=models.ListRevisionsOutputBody(items=[], limit=2, offset=0).to_dict(),
        ),
        httpx2.Response(
            200,
            json=models.BooksOutputBody(items=[], limit=2, offset=0, total=0).to_dict(),
        ),
    ]
    client = make_client(sequence(seen_requests, responses))

    assert [recipe async for recipe in client.iter_recipes(limit=2)] == []
    assert [revision async for revision in client.iter_recipe_revisions("recipe-1", limit=2)] == []
    assert [book async for book in client.iter_books(limit=2)] == []

    assert [request.url.params["limit"] for request in seen_requests] == ["2", "2", "2"]
    await client.aclose()


async def test_meal_calendar_and_shopping_edits(seen_requests: list[httpx2.Request]) -> None:
    meal = {
        "id": "dinner",
        "display_title": "Dinner",
        "revision": 1,
        "skipped": False,
        "created_at": "2026-01-01T12:00:00Z",
        "updated_at": "2026-01-01T12:00:00Z",
        "dishes": [],
        "date": "2026-01-02",
    }
    responses = [
        httpx2.Response(200, json={"items": [meal], "offset": 0, "limit": 1, "total": 1}),
        httpx2.Response(200, json=shopping_list().to_dict()),
        httpx2.Response(200, json=shopping_list().to_dict()),
    ]
    client = make_client(sequence(seen_requests, responses))
    meals = [m async for m in client.iter_meals(from_="2026-01-01", to="2026-01-07", limit=1)]
    assert [m.display_title for m in meals] == ["Dinner"]
    assert dict(seen_requests[0].url.params) == {
        "from": "2026-01-01",
        "to": "2026-01-07",
        "include_unscheduled": "false",
        "limit": "1",
        "offset": "0",
    }
    items = models.CreateGroceryItemsRequest(items=[models.Addition(id="a", name="Milk")])
    added = await client.create_grocery_items("list-1", items, idempotency_key="add-milk")
    assert seen_requests[1].headers["idempotency-key"] == "add-milk"
    change = models.ShoppingChange(
        base_revision=added.revision,
        id="check",
        item_id="a",
        kind=models.ShoppingChangeKind.EDIT,
        bought=True,
    )
    changed = await client.change_groceries(added.id, change)
    assert changed.id == added.id
    assert seen_requests[2].url.path.endswith("/shopping/lists/list-1/changes")
