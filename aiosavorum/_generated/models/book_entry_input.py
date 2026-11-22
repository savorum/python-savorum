from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BookEntryInput")



@_attrs_define
class BookEntryInput:
    """ 
        Attributes:
            library_entry_id (str): Identifier of the member entry in the local Savorum library
            position (int):
            id (str | Unset):
            note (str | Unset):
            section_id (str | Unset):
     """

    library_entry_id: str
    position: int
    id: str | Unset = UNSET
    note: str | Unset = UNSET
    section_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        library_entry_id = self.library_entry_id

        position = self.position

        id = self.id

        note = self.note

        section_id = self.section_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "library_entry_id": library_entry_id,
            "position": position,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if section_id is not UNSET:
            field_dict["section_id"] = section_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        library_entry_id = d.pop("library_entry_id")

        position = d.pop("position")

        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        section_id = d.pop("section_id", UNSET)

        book_entry_input = cls(
            library_entry_id=library_entry_id,
            position=position,
            id=id,
            note=note,
            section_id=section_id,
        )

        return book_entry_input

