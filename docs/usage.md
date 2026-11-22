# Usage

## Client

Create one `SavorumClient` for the lifetime of a set of related requests and use
its async context manager when it creates its own HTTP client.

```python
from aiosavorum import SavorumClient

async with SavorumClient(
    base_url="http://127.0.0.1:8080",
    token="personal-api-token",
    library_id="library-id",
) as client:
    capabilities = await client.get_capabilities()
```

The same pattern works for Savorum Cloud and self-hosted instances. Set the base
URL to the final instance address, including any path prefix. A trailing slash
is accepted. The SDK stops at redirects to keep credentials and request bodies
at the configured instance.

```python
async with SavorumClient(
    base_url="https://example.my.savorum.net/",
    token="personal-api-token",
    library_id="library-id",
) as cloud:
    capabilities = await cloud.get_capabilities()
```

An injected `httpx2.AsyncClient` remains owned by the caller. Credentials passed
to `SavorumClient` are applied per request rather than stored on the injected
client's default headers. This makes one shared client safe to use with multiple
tokens and libraries.

```python
import httpx2
from aiosavorum import SavorumClient

shared = httpx2.AsyncClient()
alice = SavorumClient(base_url="http://127.0.0.1:8080", token="alice", client=shared)
bob = SavorumClient(base_url="http://127.0.0.1:8080", token="bob", client=shared)
scoped = alice.for_library("another-library")
```

`alice` and `bob` can be used concurrently. Closing either does not close the
other or `shared`. Close the original client that created the HTTP client; a
derived client from `for_library()` shares it.

## Errors

All client errors inherit from `SavorumError`. API responses become errors with
status codes and, when the API provides one, stable error codes.

```python
from aiosavorum import AuthenticationError, NotFoundError, SavorumError

try:
    await client.get_recipe("missing")
except NotFoundError:
    ...
except AuthenticationError:
    ...
except SavorumError:
    ...
```

`PreconditionFailedError` reports a failed `If-Match` check. Its `revision`
attribute contains the server's current revision when the response provides it.
`PreconditionRequiredError` reports an endpoint that requires a revision.

`TransportError` wraps network failures. `DeserializationError` reports a
response that does not match the generated model. `ResponseDecodeError` reports
a successful response with an unexpected empty body.

## Pagination

List helpers return a `Page` with `items`, `offset`, `limit`, and `total`, and an
`iter_*` helper yields items across every page. Endpoints that omit a total set
`page.total` to `None`; pagination then continues while a full page is returned.

```python
page = await client.list_recipes_page(q="pasta", limit=25)
print(page.total)

async for recipe in client.iter_recipes(q="pasta", limit=25):
    print(recipe.id)
```

Pagination helpers cover recipes, recipe revisions, books, and meals. Use
`iter_meals(from_="2026-01-01", to="2026-01-31")` to read a calendar date
range. Each item is a `Meal`. Set `include_unscheduled=True` to include meals
without a date.

## Shopping lists

`create_grocery_items(list_id, body, idempotency_key=...)` accepts a
`models.CreateGroceryItemsRequest` containing `models.Addition` items. Reuse
the same key and item IDs when retrying an addition.

`change_groceries(list_id, body)` accepts a `models.ShoppingChange`. To check
off an item, use `models.ShoppingChangeKind.EDIT`, set `bought=True`, and
supply the item ID, change ID, and current list revision. Both methods return
the updated shopping list.

## Conditional writes

Savorum revisions are integers used with `If-Match` for update and delete
operations. An entry from a read carries its current revision.

```python
from aiosavorum import if_match_for

entry = await client.get_recipe("recipe-id")
assert entry is not None
document = entry.recipe

updated = await client.replace_recipe(
    "recipe-id",
    document,
    if_match=if_match_for(entry),
)
```

Recipe replacement, trash, and restore require a revision. Pass the integer
revision or the quoted value from `if_match_for()`. Omitting it raises
`PreconditionRequiredError` on these endpoints.

Pass a stable `idempotency_key` to create operations that may be retried. The
server returns the original result for a repeated key.

```python
entry = await client.create_recipe(document, idempotency_key="import-42")
```

## Events

`SavorumClient.events()` yields `ChangeEvent`, `ResyncEvent`, and `CursorEvent`
values from `/api/v1/events`. Events are versioned. The client records each
frame id and sends it as `Last-Event-Id` after a connection failure, subject to
the server's retained history.

```python
from aiosavorum import ChangeEvent, CursorEvent, ResyncEvent

async for event in client.events(after="last-seen-event-id"):
    if isinstance(event, ChangeEvent):
        print(event.kind, event.library_id, event.resource_id)
    elif isinstance(event, ResyncEvent):
        print("refresh local state")
    elif isinstance(event, CursorEvent):
        print("connected at", event.id)
```

`after` supplies the initial `Last-Event-Id`. It is a resume hint, not a filter:
the server may replay retained events. `resync` always means local derived state
must be rebuilt from the API. Heartbeats are consumed by the SSE reader and do
not appear as events.

The subscription reconnects with exponential backoff after transport errors, rate limits, and
server failures. Authentication and authorization errors reach the caller.
Set `reconnect=False` to let an error propagate. Resume from the last yielded
`event.id` when restarting a process.

## Raw and generated requests

`SavorumClient.api` exposes the generated endpoint modules by tag. It invokes
the generated request and response helpers while executing on the configured
`httpx2.AsyncClient`.

```python
from aiosavorum import SavorumClient

client = SavorumClient(base_url="http://127.0.0.1:8080")
recipes = await client.api.recipes.list_recipes(limit=10)
```

`client.request()` sends a raw request with the configured credentials. Use it
for responses the generator omits, including binary downloads.

```python
response = await client.request("GET", "/api/v1/recipes/recipe-id/export")
data = response.content
```

`from aiosavorum import generated` exposes the pinned generated client. Import
endpoint modules from it when a wrapper does not cover an operation, and
construct generated request models from `aiosavorum.models`.
