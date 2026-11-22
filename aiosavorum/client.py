"""Ergonomic async client for the Savorum HTTP API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, TypeVar, cast

import httpx2

from ._generated.api.account import get_current_account as _get_current_account_endpoint
from ._generated.api.api_tokens import list_account_tokens as _list_account_tokens_endpoint
from ._generated.api.books import get_book as _get_book_endpoint
from ._generated.api.books import list_books as _list_books_endpoint
from ._generated.api.instance import get_capabilities as _get_capabilities_endpoint
from ._generated.api.instance import get_health as _get_health_endpoint
from ._generated.api.libraries import list_libraries as _list_libraries_endpoint
from ._generated.api.plan import list_meals as _list_meals_endpoint
from ._generated.api.recipes import create_recipe as _create_recipe_endpoint
from ._generated.api.recipes import get_recipe as _get_recipe_endpoint
from ._generated.api.recipes import get_recipe_revision as _get_recipe_revision_endpoint
from ._generated.api.recipes import list_recipe_revisions as _list_recipe_revisions_endpoint
from ._generated.api.recipes import list_recipes as _list_recipes_endpoint
from ._generated.api.recipes import replace_recipe as _replace_recipe_endpoint
from ._generated.api.recipes import restore_recipe as _restore_recipe_endpoint
from ._generated.api.recipes import trash_recipe as _trash_recipe_endpoint
from ._generated.api.shopping import change_groceries as _change_groceries_endpoint
from ._generated.api.shopping import create_grocery_items as _create_grocery_items_endpoint
from ._generated.api.shopping import create_shopping_list as _create_shopping_list_endpoint
from ._generated.api.shopping import get_groceries as _get_groceries_endpoint
from ._generated.api.shopping import list_shopping_lists as _list_shopping_lists_endpoint
from ._generated.types import UNSET
from ._transport import (
    ApiProxy,
    _EndpointModule,
    raise_response_error,
)
from .errors import ResponseDecodeError
from .events import subscribe_events
from .pagination import Page, iter_page_items

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator, AsyncIterator, Mapping, Sequence

    from ._generated.types import Unset
    from .events import StreamEvent
    from .models import (
        AccountState,
        Book,
        BooksOutputBody,
        BookSummary,
        Capabilities,
        CreateGroceryItemsRequest,
        HealthOutputBody,
        LibrariesResponse,
        Library,
        LibraryEntry,
        ListBooksState,
        ListRecipesOutputBody,
        ListRecipesSort,
        ListRecipesState,
        ListRevisionsOutputBody,
        Meal,
        MealsOutputBody,
        RecipeDocument,
        RecipeRevision,
        RecipeRevisionSummary,
        RecipeSummary,
        ShoppingChange,
        ShoppingList,
        ShoppingListInput,
        ShoppingListSummary,
        TokenListResponse,
    )

T = TypeVar("T")

DEFAULT_BASE_URL = "http://127.0.0.1:8080"
DEFAULT_USER_AGENT = "aiosavorum/0.1.0"

_LIST_MEALS = cast("_EndpointModule", _list_meals_endpoint)
_CREATE_GROCERY_ITEMS = cast("_EndpointModule", _create_grocery_items_endpoint)
_CHANGE_GROCERIES = cast("_EndpointModule", _change_groceries_endpoint)
_HEALTH = cast("_EndpointModule", _get_health_endpoint)
_CAPABILITIES = cast("_EndpointModule", _get_capabilities_endpoint)
_CURRENT_ACCOUNT = cast("_EndpointModule", _get_current_account_endpoint)
_LIST_TOKENS = cast("_EndpointModule", _list_account_tokens_endpoint)
_LIST_LIBRARIES = cast("_EndpointModule", _list_libraries_endpoint)
_LIST_RECIPES = cast("_EndpointModule", _list_recipes_endpoint)
_GET_RECIPE = cast("_EndpointModule", _get_recipe_endpoint)
_CREATE_RECIPE = cast("_EndpointModule", _create_recipe_endpoint)
_REPLACE_RECIPE = cast("_EndpointModule", _replace_recipe_endpoint)
_TRASH_RECIPE = cast("_EndpointModule", _trash_recipe_endpoint)
_RESTORE_RECIPE = cast("_EndpointModule", _restore_recipe_endpoint)
_LIST_RECIPE_REVISIONS = cast("_EndpointModule", _list_recipe_revisions_endpoint)
_GET_RECIPE_REVISION = cast("_EndpointModule", _get_recipe_revision_endpoint)
_LIST_BOOKS = cast("_EndpointModule", _list_books_endpoint)
_GET_BOOK = cast("_EndpointModule", _get_book_endpoint)
_LIST_SHOPPING_LISTS = cast("_EndpointModule", _list_shopping_lists_endpoint)
_GET_GROCERIES = cast("_EndpointModule", _get_groceries_endpoint)
_CREATE_SHOPPING_LIST = cast("_EndpointModule", _create_shopping_list_endpoint)


def _optional(value: T | None) -> T | Unset:
    return UNSET if value is None else value


def _if_match(value: str | int | None) -> str | Unset:
    if value is None:
        return UNSET
    text = str(value)
    return f'"{text}"' if text.isdecimal() else text


def _require(value: T | None, message: str) -> T:
    if value is None:
        raise ResponseDecodeError(message)
    return value


def if_match_for(entry: LibraryEntry) -> str:
    """Return the strong If-Match value for a library entry's revision."""
    return f'"{entry.revision}"'


class SavorumClient:
    """Async Savorum API client.

    Supply a personal API token for authenticated instances. Local instances in
    local mode need no token. An injected ``httpx2.AsyncClient`` remains owned
    by the caller; this client never closes it.
    """

    def __init__(
        self,
        *,
        base_url: str = DEFAULT_BASE_URL,
        token: str | None = None,
        library_id: str | None = None,
        client: httpx2.AsyncClient | None = None,
        timeout: float | httpx2.Timeout | None = None,
        user_agent: str = DEFAULT_USER_AGENT,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._token = token
        self._library_id = library_id
        self._user_agent = user_agent
        self._owns_client = client is None
        self._closed = False

        headers = {"Accept": "application/json", "User-Agent": user_agent}
        if token is not None:
            headers["Authorization"] = f"Bearer {token}"
        if library_id is not None:
            headers["X-Savorum-Library"] = library_id
        self._headers = headers

        if client is None:
            client = httpx2.AsyncClient(
                base_url=self._base_url,
                headers=headers,
                timeout=timeout,
            )
        self._http_client = client

        from ._transport import _RequestExecutor

        self._executor = _RequestExecutor(
            base_url=self._base_url,
            headers=self._headers,
            http_client=self._http_client,
        )
        self.api = ApiProxy(self._executor)

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def owns_client(self) -> bool:
        """Whether this client closes its HTTPX2 client on exit."""
        return self._owns_client

    def for_library(self, library_id: str) -> SavorumClient:
        """Return a client scoped to another library.

        The returned client shares this client's HTTPX2 client and does not
        close it. Close the original client to release a client it created.
        """
        return SavorumClient(
            base_url=self._base_url,
            token=self._token,
            library_id=library_id,
            client=self._http_client,
            user_agent=self._user_agent,
        )

    async def aclose(self) -> None:
        """Close the HTTPX2 client when this client created it."""
        if self._owns_client and not self._closed:
            self._closed = True
            await self._http_client.aclose()

    async def __aenter__(self) -> SavorumClient:
        return self

    async def __aexit__(self, *args: object) -> None:
        await self.aclose()

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
        raise_for_status: bool = True,
    ) -> httpx2.Response:
        """Issue a raw request with credentials applied.

        Use this for endpoints whose binary responses the generator omits.
        """
        response = await self._executor.request(
            method,
            path,
            params=params,
            json=json,
            content=content,
            headers=headers,
            request_timeout=request_timeout,
        )
        if raise_for_status:
            raise_response_error(response)
        return response

    def events(
        self,
        *,
        after: str | None = None,
        reconnect: bool = True,
        initial_backoff: float = 0.5,
        max_backoff: float = 30.0,
        jitter: float = 0.1,
    ) -> AsyncGenerator[StreamEvent, None]:
        """Subscribe to versioned library events with native HTTPX2 SSE."""
        return subscribe_events(
            self._http_client,
            self._executor.url("/api/v1/events"),
            self._headers,
            after=after,
            reconnect=reconnect,
            initial_backoff=initial_backoff,
            max_backoff=max_backoff,
            jitter=jitter,
        )

    async def get_health(self) -> HealthOutputBody | None:
        return cast("HealthOutputBody | None", await self._executor.call_endpoint(_HEALTH))

    async def get_capabilities(self) -> Capabilities:
        result = await self._executor.call_endpoint(_CAPABILITIES)
        return cast("Capabilities", _require(result, "Capabilities response was empty"))

    async def get_current_account(self) -> AccountState:
        result = await self._executor.call_endpoint(_CURRENT_ACCOUNT)
        return cast("AccountState", _require(result, "Account response was empty"))

    async def list_account_tokens(self) -> TokenListResponse:
        result = await self._executor.call_endpoint(_LIST_TOKENS)
        return cast("TokenListResponse", _require(result, "Token response was empty"))

    async def list_libraries(self) -> list[Library]:
        result = await self._executor.call_endpoint(_LIST_LIBRARIES)
        libraries = cast("LibrariesResponse", result).libraries
        return list(libraries or [])

    async def list_recipes_page(
        self,
        *,
        q: str | None = None,
        state: ListRecipesState | None = None,
        sort: ListRecipesSort | None = None,
        seed: int | None = None,
        group_translations: bool | None = None,
        languages: str | None = None,
        limit: int = 50,
        offset: int = 0,
    ) -> Page[RecipeSummary]:
        result = await self._executor.call_endpoint(
            _LIST_RECIPES,
            q=_optional(q),
            state=_optional(state),
            sort=_optional(sort),
            seed=_optional(seed),
            group_translations=_optional(group_translations),
            languages=_optional(languages),
            limit=limit,
            offset=offset,
        )
        output = cast("ListRecipesOutputBody | None", result)
        return _page(output, offset=offset, limit=limit)

    def iter_recipes(
        self,
        *,
        q: str | None = None,
        state: ListRecipesState | None = None,
        sort: ListRecipesSort | None = None,
        seed: int | None = None,
        group_translations: bool | None = None,
        languages: str | None = None,
        limit: int = 50,
    ) -> AsyncIterator[RecipeSummary]:
        return iter_page_items(
            lambda offset, page_limit: self.list_recipes_page(
                q=q,
                state=state,
                sort=sort,
                seed=seed,
                group_translations=group_translations,
                languages=languages,
                limit=page_limit,
                offset=offset,
            ),
            limit=limit,
        )

    async def get_recipe(self, recipe_id: str) -> LibraryEntry | None:
        result = await self._executor.call_endpoint(_GET_RECIPE, id=recipe_id)
        return cast("LibraryEntry | None", result)

    async def create_recipe(
        self,
        body: RecipeDocument,
        *,
        idempotency_key: str | None = None,
    ) -> LibraryEntry:
        result = await self._executor.call_endpoint(
            _CREATE_RECIPE,
            body=body,
            idempotency_key=_optional(idempotency_key),
        )
        return cast("LibraryEntry", _require(result, "Create recipe response was empty"))

    async def replace_recipe(
        self,
        recipe_id: str,
        body: RecipeDocument,
        *,
        if_match: str | int | None = None,
    ) -> LibraryEntry:
        result = await self._executor.call_endpoint(
            _REPLACE_RECIPE,
            id=recipe_id,
            body=body,
            if_match=_if_match(if_match),
        )
        return cast("LibraryEntry", _require(result, "Replace recipe response was empty"))

    async def trash_recipe(
        self,
        recipe_id: str,
        *,
        if_match: str | int | None = None,
    ) -> LibraryEntry:
        result = await self._executor.call_endpoint(
            _TRASH_RECIPE,
            id=recipe_id,
            if_match=_if_match(if_match),
        )
        return cast("LibraryEntry", _require(result, "Trash recipe response was empty"))

    async def restore_recipe(
        self,
        recipe_id: str,
        *,
        if_match: str | int | None = None,
    ) -> LibraryEntry:
        result = await self._executor.call_endpoint(
            _RESTORE_RECIPE,
            id=recipe_id,
            if_match=_if_match(if_match),
        )
        return cast("LibraryEntry", _require(result, "Restore recipe response was empty"))

    async def list_recipe_revisions_page(
        self,
        recipe_id: str,
        *,
        limit: int = 50,
        offset: int = 0,
    ) -> Page[RecipeRevisionSummary]:
        result = await self._executor.call_endpoint(
            _LIST_RECIPE_REVISIONS,
            id=recipe_id,
            limit=limit,
            offset=offset,
        )
        output = cast("ListRevisionsOutputBody | None", result)
        return _page(output, offset=offset, limit=limit)

    def iter_recipe_revisions(
        self,
        recipe_id: str,
        *,
        limit: int = 50,
    ) -> AsyncIterator[RecipeRevisionSummary]:
        return iter_page_items(
            lambda offset, page_limit: self.list_recipe_revisions_page(
                recipe_id,
                limit=page_limit,
                offset=offset,
            ),
            limit=limit,
        )

    async def get_recipe_revision(
        self,
        recipe_id: str,
        revision: int,
    ) -> RecipeRevision:
        result = await self._executor.call_endpoint(
            _GET_RECIPE_REVISION,
            id=recipe_id,
            revision=revision,
        )
        return cast(
            "RecipeRevision",
            _require(result, "Recipe revision response was empty"),
        )

    async def list_books_page(
        self,
        *,
        entry_id: str | None = None,
        state: ListBooksState | None = None,
        limit: int = 50,
        offset: int = 0,
    ) -> Page[BookSummary]:
        result = await self._executor.call_endpoint(
            _LIST_BOOKS,
            entry_id=_optional(entry_id),
            state=_optional(state),
            limit=limit,
            offset=offset,
        )
        return _page(cast("BooksOutputBody | None", result), offset=offset, limit=limit)

    def iter_books(
        self,
        *,
        entry_id: str | None = None,
        state: ListBooksState | None = None,
        limit: int = 50,
    ) -> AsyncIterator[BookSummary]:
        return iter_page_items(
            lambda offset, page_limit: self.list_books_page(
                entry_id=entry_id,
                state=state,
                limit=page_limit,
                offset=offset,
            ),
            limit=limit,
        )

    async def get_book(self, book_id: str) -> Book | None:
        result = await self._executor.call_endpoint(_GET_BOOK, id=book_id)
        return cast("Book | None", result)

    async def list_meals_page(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        include_unscheduled: bool = False,
        limit: int = 50,
        offset: int = 0,
    ) -> Page[Meal]:
        result = await self._executor.call_endpoint(
            _LIST_MEALS,
            from_=_optional(from_),
            to=_optional(to),
            include_unscheduled=include_unscheduled,
            limit=limit,
            offset=offset,
        )
        return _page(cast("MealsOutputBody", result), offset=offset, limit=limit)

    def iter_meals(
        self,
        *,
        from_: str | None = None,
        to: str | None = None,
        include_unscheduled: bool = False,
        limit: int = 50,
    ) -> AsyncIterator[Meal]:
        return iter_page_items(
            lambda offset, page_limit: self.list_meals_page(
                from_=from_,
                to=to,
                include_unscheduled=include_unscheduled,
                limit=page_limit,
                offset=offset,
            ),
            limit=limit,
        )

    async def create_grocery_items(
        self,
        list_id: str,
        body: CreateGroceryItemsRequest,
        *,
        idempotency_key: str,
    ) -> ShoppingList:
        result = await self._executor.call_endpoint(
            _CREATE_GROCERY_ITEMS,
            list_id=list_id,
            body=body,
            idempotency_key=idempotency_key,
        )
        return cast("ShoppingList", _require(result, "Groceries response was empty"))

    async def change_groceries(
        self,
        list_id: str,
        body: ShoppingChange,
        *,
        idempotency_key: str | None = None,
    ) -> ShoppingList:
        result = await self._executor.call_endpoint(
            _CHANGE_GROCERIES,
            list_id=list_id,
            body=body,
            idempotency_key=_optional(idempotency_key),
        )
        return cast("ShoppingList", _require(result, "Groceries response was empty"))

    async def list_shopping_lists(self) -> list[ShoppingListSummary]:
        result = await self._executor.call_endpoint(_LIST_SHOPPING_LISTS)
        return list(cast("list[ShoppingListSummary] | None", result) or [])

    async def get_groceries(self, list_id: str) -> ShoppingList:
        result = await self._executor.call_endpoint(_GET_GROCERIES, list_id=list_id)
        return cast("ShoppingList", _require(result, "Groceries response was empty"))

    async def create_shopping_list(
        self,
        body: ShoppingListInput,
        *,
        idempotency_key: str | None = None,
    ) -> ShoppingList:
        result = await self._executor.call_endpoint(
            _CREATE_SHOPPING_LIST,
            body=body,
            idempotency_key=_optional(idempotency_key),
        )
        return cast("ShoppingList", _require(result, "Shopping list response was empty"))


T_co = TypeVar("T_co", covariant=True)


class _PageBody(Protocol[T_co]):
    @property
    def items(self) -> Sequence[T_co] | None: ...
    @property
    def limit(self) -> int: ...
    @property
    def offset(self) -> int: ...


def _page(output: _PageBody[T] | None, *, offset: int, limit: int) -> Page[T]:
    if output is None:
        return Page((), offset, limit, offset)
    items = tuple(output.items or ())
    total = getattr(output, "total", None)
    return Page(
        items=items,
        offset=output.offset,
        limit=output.limit,
        total=int(total) if total is not None else None,
    )
