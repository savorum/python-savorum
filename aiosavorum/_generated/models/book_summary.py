from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.book_summary_kind import BookSummaryKind
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="BookSummary")



@_attrs_define
class BookSummary:
    """ 
        Attributes:
            entry_count (int):
            id (str):
            kind (BookSummaryKind):
            revision (int):
            title (str):
            updated_at (datetime.datetime):
            author (str | Unset):
            contains_entry (bool | Unset):
            cover_asset_id (str | Unset):
            deleted_at (datetime.datetime | Unset):
            preview_asset_id (str | Unset): A recipe photograph for a book without a cover
            preview_entry_id (str | Unset): The accessible recipe that scopes the preview photograph
     """

    entry_count: int
    id: str
    kind: BookSummaryKind
    revision: int
    title: str
    updated_at: datetime.datetime
    author: str | Unset = UNSET
    contains_entry: bool | Unset = UNSET
    cover_asset_id: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    preview_asset_id: str | Unset = UNSET
    preview_entry_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        entry_count = self.entry_count

        id = self.id

        kind = self.kind.value

        revision = self.revision

        title = self.title

        updated_at = self.updated_at.isoformat()

        author = self.author

        contains_entry = self.contains_entry

        cover_asset_id = self.cover_asset_id

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        preview_asset_id = self.preview_asset_id

        preview_entry_id = self.preview_entry_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "entry_count": entry_count,
            "id": id,
            "kind": kind,
            "revision": revision,
            "title": title,
            "updated_at": updated_at,
        })
        if author is not UNSET:
            field_dict["author"] = author
        if contains_entry is not UNSET:
            field_dict["contains_entry"] = contains_entry
        if cover_asset_id is not UNSET:
            field_dict["cover_asset_id"] = cover_asset_id
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if preview_asset_id is not UNSET:
            field_dict["preview_asset_id"] = preview_asset_id
        if preview_entry_id is not UNSET:
            field_dict["preview_entry_id"] = preview_entry_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry_count = d.pop("entry_count")

        id = d.pop("id")

        kind = BookSummaryKind(d.pop("kind"))




        revision = d.pop("revision")

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        author = d.pop("author", UNSET)

        contains_entry = d.pop("contains_entry", UNSET)

        cover_asset_id = d.pop("cover_asset_id", UNSET)

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at,  Unset):
            deleted_at = UNSET
        else:
            deleted_at = datetime.datetime.fromisoformat(_deleted_at)




        preview_asset_id = d.pop("preview_asset_id", UNSET)

        preview_entry_id = d.pop("preview_entry_id", UNSET)

        book_summary = cls(
            entry_count=entry_count,
            id=id,
            kind=kind,
            revision=revision,
            title=title,
            updated_at=updated_at,
            author=author,
            contains_entry=contains_entry,
            cover_asset_id=cover_asset_id,
            deleted_at=deleted_at,
            preview_asset_id=preview_asset_id,
            preview_entry_id=preview_entry_id,
        )


        book_summary.additional_properties = d
        return book_summary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
