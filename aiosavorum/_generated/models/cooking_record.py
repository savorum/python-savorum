from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CookingRecord")



@_attrs_define
class CookingRecord:
    """ 
        Attributes:
            cooked_on (datetime.date):
            created_at (datetime.datetime):
            id (str):
            cooked_time (str | Unset):
            note (str | Unset):
            scale (str | Unset): Batch actually made, as a factor of the recipe as written
            session_id (str | Unset):
     """

    cooked_on: datetime.date
    created_at: datetime.datetime
    id: str
    cooked_time: str | Unset = UNSET
    note: str | Unset = UNSET
    scale: str | Unset = UNSET
    session_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cooked_on = self.cooked_on.isoformat()

        created_at = self.created_at.isoformat()

        id = self.id

        cooked_time = self.cooked_time

        note = self.note

        scale = self.scale

        session_id = self.session_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cooked_on": cooked_on,
            "created_at": created_at,
            "id": id,
        })
        if cooked_time is not UNSET:
            field_dict["cooked_time"] = cooked_time
        if note is not UNSET:
            field_dict["note"] = note
        if scale is not UNSET:
            field_dict["scale"] = scale
        if session_id is not UNSET:
            field_dict["session_id"] = session_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cooked_on = datetime.date.fromisoformat(d.pop("cooked_on"))




        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        cooked_time = d.pop("cooked_time", UNSET)

        note = d.pop("note", UNSET)

        scale = d.pop("scale", UNSET)

        session_id = d.pop("session_id", UNSET)

        cooking_record = cls(
            cooked_on=cooked_on,
            created_at=created_at,
            id=id,
            cooked_time=cooked_time,
            note=note,
            scale=scale,
            session_id=session_id,
        )


        cooking_record.additional_properties = d
        return cooking_record

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
