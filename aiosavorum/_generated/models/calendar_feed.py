from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CalendarFeed")



@_attrs_define
class CalendarFeed:
    """ 
        Attributes:
            created_at (datetime.datetime):
            created_by (str):
            created_by_name (str):
            id (str):
            mine (bool):
            name (str):
            last_read_at (datetime.datetime | Unset):
            rotated_at (datetime.datetime | Unset):
     """

    created_at: datetime.datetime
    created_by: str
    created_by_name: str
    id: str
    mine: bool
    name: str
    last_read_at: datetime.datetime | Unset = UNSET
    rotated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        created_by_name = self.created_by_name

        id = self.id

        mine = self.mine

        name = self.name

        last_read_at: str | Unset = UNSET
        if not isinstance(self.last_read_at, Unset):
            last_read_at = self.last_read_at.isoformat()

        rotated_at: str | Unset = UNSET
        if not isinstance(self.rotated_at, Unset):
            rotated_at = self.rotated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "created_by": created_by,
            "created_by_name": created_by_name,
            "id": id,
            "mine": mine,
            "name": name,
        })
        if last_read_at is not UNSET:
            field_dict["last_read_at"] = last_read_at
        if rotated_at is not UNSET:
            field_dict["rotated_at"] = rotated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        created_by = d.pop("created_by")

        created_by_name = d.pop("created_by_name")

        id = d.pop("id")

        mine = d.pop("mine")

        name = d.pop("name")

        _last_read_at = d.pop("last_read_at", UNSET)
        last_read_at: datetime.datetime | Unset
        if isinstance(_last_read_at,  Unset):
            last_read_at = UNSET
        else:
            last_read_at = datetime.datetime.fromisoformat(_last_read_at)




        _rotated_at = d.pop("rotated_at", UNSET)
        rotated_at: datetime.datetime | Unset
        if isinstance(_rotated_at,  Unset):
            rotated_at = UNSET
        else:
            rotated_at = datetime.datetime.fromisoformat(_rotated_at)




        calendar_feed = cls(
            created_at=created_at,
            created_by=created_by,
            created_by_name=created_by_name,
            id=id,
            mine=mine,
            name=name,
            last_read_at=last_read_at,
            rotated_at=rotated_at,
        )


        calendar_feed.additional_properties = d
        return calendar_feed

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
