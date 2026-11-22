from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BookSelectionSummary")



@_attrs_define
class BookSelectionSummary:
    """ 
        Attributes:
            id (str):
            kind (str):
            revision (int):
            title (str):
            author (str | Unset):
            cover_asset_id (str | Unset):
            edition (str | Unset):
            editor (str | Unset):
            subtitle (str | Unset):
     """

    id: str
    kind: str
    revision: int
    title: str
    author: str | Unset = UNSET
    cover_asset_id: str | Unset = UNSET
    edition: str | Unset = UNSET
    editor: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        revision = self.revision

        title = self.title

        author = self.author

        cover_asset_id = self.cover_asset_id

        edition = self.edition

        editor = self.editor

        subtitle = self.subtitle


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "kind": kind,
            "revision": revision,
            "title": title,
        })
        if author is not UNSET:
            field_dict["author"] = author
        if cover_asset_id is not UNSET:
            field_dict["cover_asset_id"] = cover_asset_id
        if edition is not UNSET:
            field_dict["edition"] = edition
        if editor is not UNSET:
            field_dict["editor"] = editor
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        kind = d.pop("kind")

        revision = d.pop("revision")

        title = d.pop("title")

        author = d.pop("author", UNSET)

        cover_asset_id = d.pop("cover_asset_id", UNSET)

        edition = d.pop("edition", UNSET)

        editor = d.pop("editor", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        book_selection_summary = cls(
            id=id,
            kind=kind,
            revision=revision,
            title=title,
            author=author,
            cover_asset_id=cover_asset_id,
            edition=edition,
            editor=editor,
            subtitle=subtitle,
        )


        book_selection_summary.additional_properties = d
        return book_selection_summary

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
