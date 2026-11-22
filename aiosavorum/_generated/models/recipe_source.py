from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.recipe_source_kind import RecipeSourceKind
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="RecipeSource")



@_attrs_define
class RecipeSource:
    """ 
        Attributes:
            kind (RecipeSourceKind):
            accessed_at (datetime.datetime | Unset):
            attribution (str | Unset):
            id (str | Unset):
            original_title (str | Unset):
            page_end (int | Unset):
            page_start (int | Unset):
            publication_book_id (str | Unset):
            url (str | Unset):
     """

    kind: RecipeSourceKind
    accessed_at: datetime.datetime | Unset = UNSET
    attribution: str | Unset = UNSET
    id: str | Unset = UNSET
    original_title: str | Unset = UNSET
    page_end: int | Unset = UNSET
    page_start: int | Unset = UNSET
    publication_book_id: str | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        accessed_at: str | Unset = UNSET
        if not isinstance(self.accessed_at, Unset):
            accessed_at = self.accessed_at.isoformat()

        attribution = self.attribution

        id = self.id

        original_title = self.original_title

        page_end = self.page_end

        page_start = self.page_start

        publication_book_id = self.publication_book_id

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })
        if accessed_at is not UNSET:
            field_dict["accessed_at"] = accessed_at
        if attribution is not UNSET:
            field_dict["attribution"] = attribution
        if id is not UNSET:
            field_dict["id"] = id
        if original_title is not UNSET:
            field_dict["original_title"] = original_title
        if page_end is not UNSET:
            field_dict["page_end"] = page_end
        if page_start is not UNSET:
            field_dict["page_start"] = page_start
        if publication_book_id is not UNSET:
            field_dict["publication_book_id"] = publication_book_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = RecipeSourceKind(d.pop("kind"))




        _accessed_at = d.pop("accessed_at", UNSET)
        accessed_at: datetime.datetime | Unset
        if isinstance(_accessed_at,  Unset):
            accessed_at = UNSET
        else:
            accessed_at = datetime.datetime.fromisoformat(_accessed_at)




        attribution = d.pop("attribution", UNSET)

        id = d.pop("id", UNSET)

        original_title = d.pop("original_title", UNSET)

        page_end = d.pop("page_end", UNSET)

        page_start = d.pop("page_start", UNSET)

        publication_book_id = d.pop("publication_book_id", UNSET)

        url = d.pop("url", UNSET)

        recipe_source = cls(
            kind=kind,
            accessed_at=accessed_at,
            attribution=attribution,
            id=id,
            original_title=original_title,
            page_end=page_end,
            page_start=page_start,
            publication_book_id=publication_book_id,
            url=url,
        )

        return recipe_source

