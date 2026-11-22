from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="User")



@_attrs_define
class User:
    """ 
        Attributes:
            created_at (datetime.datetime):
            display_name (str):
            instance_admin (bool):
            status (str):
            user_id (str):
     """

    created_at: datetime.datetime
    display_name: str
    instance_admin: bool
    status: str
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        display_name = self.display_name

        instance_admin = self.instance_admin

        status = self.status

        user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "display_name": display_name,
            "instance_admin": instance_admin,
            "status": status,
            "user_id": user_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        display_name = d.pop("display_name")

        instance_admin = d.pop("instance_admin")

        status = d.pop("status")

        user_id = d.pop("user_id")

        user = cls(
            created_at=created_at,
            display_name=display_name,
            instance_admin=instance_admin,
            status=status,
            user_id=user_id,
        )


        user.additional_properties = d
        return user

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
