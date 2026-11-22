"""Pagination helper tests."""

from __future__ import annotations

from aiosavorum import Page
from aiosavorum.pagination import iter_page_items


def test_page_reports_next_only_when_items_remain() -> None:
    assert Page((1, 2), 0, 2, 4).has_next is True
    assert Page((1, 2), 2, 2, 4).has_next is False
    assert Page((), 0, 2, 4).has_next is True
    assert Page((1, 2), 0, 2).total is None
    assert Page((1, 2), 0, 2).has_next is True
    assert Page((1,), 0, 2).has_next is False


async def test_iter_page_items_walks_offsets() -> None:
    pages = [
        Page((1, 2), 0, 2, 5),
        Page((3, 4), 2, 2, 5),
        Page((5,), 4, 2, 5),
    ]
    requested: list[tuple[int, int]] = []

    async def fetch(offset: int, limit: int) -> Page[int]:
        requested.append((offset, limit))
        return pages[offset // limit]

    assert [item async for item in iter_page_items(fetch, limit=2)] == [1, 2, 3, 4, 5]
    assert requested == [(0, 2), (2, 2), (4, 2)]


async def test_iter_page_items_stops_on_empty_page() -> None:
    async def fetch(offset: int, limit: int) -> Page[int]:
        return Page((), offset, limit, 0)

    assert [item async for item in iter_page_items(fetch)] == []
