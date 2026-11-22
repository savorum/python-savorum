from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="PantryEntryInput")



@_attrs_define
class PantryEntryInput:
    """ 
        Attributes:
            name (str):
            amount (str | Unset):
            best_before (datetime.date | Unset):
            location (str | Unset):
            note (str | Unset):
            semantic_id (str | Unset):
            unit (str | Unset):
     """

    name: str
    amount: str | Unset = UNSET
    best_before: datetime.date | Unset = UNSET
    location: str | Unset = UNSET
    note: str | Unset = UNSET
    semantic_id: str | Unset = UNSET
    unit: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        amount = self.amount

        best_before: str | Unset = UNSET
        if not isinstance(self.best_before, Unset):
            best_before = self.best_before.isoformat()

        location = self.location

        note = self.note

        semantic_id = self.semantic_id

        unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if best_before is not UNSET:
            field_dict["best_before"] = best_before
        if location is not UNSET:
            field_dict["location"] = location
        if note is not UNSET:
            field_dict["note"] = note
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        amount = d.pop("amount", UNSET)

        _best_before = d.pop("best_before", UNSET)
        best_before: datetime.date | Unset
        if isinstance(_best_before,  Unset):
            best_before = UNSET
        else:
            best_before = datetime.date.fromisoformat(_best_before)




        location = d.pop("location", UNSET)

        note = d.pop("note", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        unit = d.pop("unit", UNSET)

        pantry_entry_input = cls(
            name=name,
            amount=amount,
            best_before=best_before,
            location=location,
            note=note,
            semantic_id=semantic_id,
            unit=unit,
        )

        return pantry_entry_input

