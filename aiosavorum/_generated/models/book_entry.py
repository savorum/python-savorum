from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.book_entry_recipe_state import BookEntryRecipeState
from ..types import UNSET, Unset






T = TypeVar("T", bound="BookEntry")



@_attrs_define
class BookEntry:
    """ 
        Attributes:
            library_entry_id (str): Identifier of the member entry in the local Savorum library
            position (int):
            recipe_state (BookEntryRecipeState): Derived recipe state. Omit this field from book write entries.
            id (str | Unset):
            note (str | Unset):
            section_id (str | Unset):
     """

    library_entry_id: str
    position: int
    recipe_state: BookEntryRecipeState
    id: str | Unset = UNSET
    note: str | Unset = UNSET
    section_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        library_entry_id = self.library_entry_id

        position = self.position

        recipe_state = self.recipe_state.value

        id = self.id

        note = self.note

        section_id = self.section_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "library_entry_id": library_entry_id,
            "position": position,
            "recipe_state": recipe_state,
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

        recipe_state = BookEntryRecipeState(d.pop("recipe_state"))




        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        section_id = d.pop("section_id", UNSET)

        book_entry = cls(
            library_entry_id=library_entry_id,
            position=position,
            recipe_state=recipe_state,
            id=id,
            note=note,
            section_id=section_id,
        )


        book_entry.additional_properties = d
        return book_entry

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
