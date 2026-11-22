# Python: Savorum (aiosavorum)

Async Python client for Savorum.

## About

`aiosavorum` is a typed async client for the Savorum HTTP API. It wraps a pinned
generated HTTPX2 client with authentication, library scoping, pagination, typed
errors, and native server-sent events. Applications can supply their own `httpx2.AsyncClient` to share connections.
The SDK supports personal tokens, local mode, Savorum Cloud, and self-hosted servers.

## Installation

Python 3.11 or later.

```sh
pip install aiosavorum
```

## Example

```python
import asyncio

from aiosavorum import SavorumClient


async def main() -> None:
    async with SavorumClient(
        base_url="http://127.0.0.1:8080",
        token="replace-with-a-personal-api-token",
        library_id="replace-with-a-library-id",
    ) as client:
        account = await client.get_current_account()
        print(account.active_library_id)

        async for recipe in client.iter_recipes(limit=50):
            print(recipe.id, recipe.title)


asyncio.run(main())
```

For Savorum Cloud, use the URL of your instance:

```python
async with SavorumClient(
    base_url="https://example.my.savorum.net/",
    token="replace-with-a-personal-api-token",
    library_id="replace-with-a-library-id",
) as client:
    account = await client.get_current_account()
```

Local instances in local mode need neither `token` nor `library_id`. Set
`base_url` to the instance's origin, including any reverse-proxy path prefix.
A trailing slash is accepted.

## Injected HTTP clients

Pass an `httpx2.AsyncClient` to share connection pools, proxies, TLS settings,
and browser-session cookies with the rest of an application. The caller keeps
ownership: `SavorumClient.aclose()` and its async context manager never close an
injected client.

```python
import httpx2
from aiosavorum import SavorumClient

http_client = httpx2.AsyncClient(cookies={"session": "..."})
client = SavorumClient(base_url="http://127.0.0.1:8080", client=http_client)
```

Credentials supplied directly to `SavorumClient` are applied per request, so an
injected client's default headers are not modified. Use `for_library()` to
derive a client for another library; the derived client shares the same HTTP
client.

## Events

`events()` uses HTTPX2's native SSE support. The API sends `change`, `resync`,
and `cursor` frames. Each frame has a durable id that the subscription uses for
`Last-Event-Id` reconnects.

```python
from aiosavorum import ChangeEvent, ResyncEvent

async for event in client.events():
    if isinstance(event, ChangeEvent):
        print(event.kind, event.library_id, event.resource_id)
    elif isinstance(event, ResyncEvent):
        print("reload local state")
```

Subscriptions reconnect after network errors. A `resync` frame signals that
local state must be refreshed from the API. See [usage](docs/usage.md) for the
complete event contract and pagination details.

## Generated client

`from aiosavorum import generated` exposes the generated client, which mirrors
the pinned OpenAPI document. `client.api` exposes its endpoints with the
configured credentials and injected HTTP client:

```python
health = await client.api.instance.get_health()
```

Use `client.request()` for endpoints whose binary responses the generator omits.
It applies the configured credentials and returns the raw `httpx2.Response`.

## Changelog and releases

The project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Release notes
are in [CHANGELOG.md](CHANGELOG.md). Tagged `vX.Y.Z` commits build and publish
the wheel and source distribution to PyPI.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and pull request
requirements. The [code of conduct](CODE_OF_CONDUCT.md) applies in all project spaces.

## License

`aiosavorum` is MIT licensed. See [LICENSE.txt](LICENSE.txt).
