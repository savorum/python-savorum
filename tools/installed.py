#!/usr/bin/env python3
"""Exercise aiosavorum as an installed distribution rather than a checkout.

Build and install the wheel first, then run this from a directory that is not
the checkout:

    cd "$(mktemp -d)"
    python3 /path/to/python-savorum/tools/installed.py

It refuses to run if it imports the checkout instead of the installed package.
"""

from __future__ import annotations

import asyncio
import logging
import pathlib
import sys

LOGGER = logging.getLogger(__name__)


async def _smoke(installed: pathlib.Path, source: pathlib.Path) -> int:
    import httpx2

    import aiosavorum

    if installed.parent == source:
        LOGGER.error("imported the checkout at %s, not an installed distribution", installed)
        return 2
    LOGGER.info("aiosavorum %s from %s", aiosavorum.__version__, installed.parent)

    if not (installed.parent / "py.typed").is_file():
        LOGGER.error("the installed distribution is missing py.typed")
        return 1
    if not (installed.parent / "_generated" / "api" / "recipes").is_dir():
        LOGGER.error("the installed distribution is missing the generated client")
        return 1

    seen: list[httpx2.Request] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        seen.append(request)
        return httpx2.Response(200, json={"status": "ok"})

    transport = httpx2.MockTransport(handler)
    async with (
        httpx2.AsyncClient(transport=transport) as http_client,
        aiosavorum.SavorumClient(
            base_url="https://example.invalid",
            token="test-token",  # noqa: S106
            library_id="library-1",
            client=http_client,
        ) as client,
    ):
        health = await client.get_health()

    if health is None or str(health.status) != "ok":
        LOGGER.error("health response did not parse: %r", health)
        return 1
    if len(seen) != 1:
        LOGGER.error("expected one request, saw %d", len(seen))
        return 1
    request = seen[0]
    if str(request.url) != "https://example.invalid/api/v1/health":
        LOGGER.error("unexpected request URL: %s", request.url)
        return 1
    if request.headers.get("authorization") != "Bearer test-token":
        LOGGER.error("the token header is missing")
        return 1
    if request.headers.get("x-savorum-library") != "library-1":
        LOGGER.error("the library header is missing")
        return 1

    LOGGER.info("the installed client sends credentials and parses generated models")
    return 0


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    import aiosavorum

    installed = pathlib.Path(aiosavorum.__file__).resolve()
    source = pathlib.Path(__file__).resolve().parent.parent / "aiosavorum"
    return asyncio.run(_smoke(installed, source))


if __name__ == "__main__":
    sys.exit(main())
