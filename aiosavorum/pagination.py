"""Offset pagination helpers for Savorum collections."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Awaitable, Callable, Sequence

T = TypeVar("T")

__all__ = ["Page", "iter_page_items"]


@dataclass(frozen=True, slots=True)
class Page(Generic[T]):
    """One page of an offset-paginated Savorum collection."""

    items: Sequence[T]
    offset: int
    limit: int
    total: int | None = None

    @property
    def has_next(self) -> bool:
        if self.total is not None:
            return self.offset + len(self.items) < self.total
        return len(self.items) >= self.limit


async def iter_page_items(
    fetch: Callable[[int, int], Awaitable[Page[T]]],
    *,
    limit: int = 50,
) -> AsyncIterator[T]:
    """Call ``fetch(offset, limit)`` until the final page is exhausted."""
    offset = 0
    while True:
        page = await fetch(offset, limit)
        for item in page.items:
            yield item
        if not page.has_next or not page.items:
            return
        offset += len(page.items)
