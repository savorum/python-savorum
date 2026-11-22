from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Entry")



@_attrs_define
class Entry:
    """ 
        Attributes:
            id (str):
            name (str):
            revision (int):
            updated_at (datetime.datetime):
            updated_by (str):
            amount (str | Unset):
            best_before (datetime.date | Unset):
            location (str | Unset):
            note (str | Unset):
            semantic_id (str | Unset):
            unit (str | Unset):
     """

    id: str
    name: str
    revision: int
    updated_at: datetime.datetime
    updated_by: str
    amount: str | Unset = UNSET
    best_before: datetime.date | Unset = UNSET
    location: str | Unset = UNSET
    note: str | Unset = UNSET
    semantic_id: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        revision = self.revision

        updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by

        amount = self.amount

        best_before: str | Unset = UNSET
        if not isinstance(self.best_before, Unset):
            best_before = self.best_before.isoformat()

        location = self.location

        note = self.note

        semantic_id = self.semantic_id

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "revision": revision,
            "updated_at": updated_at,
            "updated_by": updated_by,
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
        id = d.pop("id")

        name = d.pop("name")

        revision = d.pop("revision")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        updated_by = d.pop("updated_by")

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

        entry = cls(
            id=id,
            name=name,
            revision=revision,
            updated_at=updated_at,
            updated_by=updated_by,
            amount=amount,
            best_before=best_before,
            location=location,
            note=note,
            semantic_id=semantic_id,
            unit=unit,
        )


        entry.additional_properties = d
        return entry

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
