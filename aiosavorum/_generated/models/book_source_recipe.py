from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BookSourceRecipe")



@_attrs_define
class BookSourceRecipe:
    """ 
        Attributes:
            library_entry_id (str): Identifier of the sourced entry in the local Savorum library
            title (str):
            original_title (str | Unset):
            page_end (int | Unset):
            page_start (int | Unset):
     """

    library_entry_id: str
    title: str
    original_title: str | Unset = UNSET
    page_end: int | Unset = UNSET
    page_start: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        library_entry_id = self.library_entry_id

        title = self.title

        original_title = self.original_title

        page_end = self.page_end

        page_start = self.page_start


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "library_entry_id": library_entry_id,
            "title": title,
        })
        if original_title is not UNSET:
            field_dict["original_title"] = original_title
        if page_end is not UNSET:
            field_dict["page_end"] = page_end
        if page_start is not UNSET:
            field_dict["page_start"] = page_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        library_entry_id = d.pop("library_entry_id")

        title = d.pop("title")

        original_title = d.pop("original_title", UNSET)

        page_end = d.pop("page_end", UNSET)

        page_start = d.pop("page_start", UNSET)

        book_source_recipe = cls(
            library_entry_id=library_entry_id,
            title=title,
            original_title=original_title,
            page_end=page_end,
            page_start=page_start,
        )


        book_source_recipe.additional_properties = d
        return book_source_recipe

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
