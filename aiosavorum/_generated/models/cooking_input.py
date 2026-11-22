from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CookingInput")



@_attrs_define
class CookingInput:
    """ 
        Attributes:
            cooked_on (datetime.date | Unset): Defaults to today
            cooked_time (str | Unset): Optional local clock time; omitted for day-only history
            note (str | Unset):
            scale (str | Unset):
            session_id (str | Unset): Cooking session key used to make retries idempotent
     """

    cooked_on: datetime.date | Unset = UNSET
    cooked_time: str | Unset = UNSET
    note: str | Unset = UNSET
    scale: str | Unset = UNSET
    session_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cooked_on: str | Unset = UNSET
        if not isinstance(self.cooked_on, Unset):
            cooked_on = self.cooked_on.isoformat()

        cooked_time = self.cooked_time

        note = self.note

        scale = self.scale

        session_id = self.session_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cooked_on is not UNSET:
            field_dict["cooked_on"] = cooked_on
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
        _cooked_on = d.pop("cooked_on", UNSET)
        cooked_on: datetime.date | Unset
        if isinstance(_cooked_on,  Unset):
            cooked_on = UNSET
        else:
            cooked_on = datetime.date.fromisoformat(_cooked_on)




        cooked_time = d.pop("cooked_time", UNSET)

        note = d.pop("note", UNSET)

        scale = d.pop("scale", UNSET)

        session_id = d.pop("session_id", UNSET)

        cooking_input = cls(
            cooked_on=cooked_on,
            cooked_time=cooked_time,
            note=note,
            scale=scale,
            session_id=session_id,
        )

        return cooking_input

