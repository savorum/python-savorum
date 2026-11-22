from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.set_member_request_role import SetMemberRequestRole






T = TypeVar("T", bound="SetMemberRequest")



@_attrs_define
class SetMemberRequest:
    """ 
        Attributes:
            role (SetMemberRequestRole):
     """

    role: SetMemberRequestRole





    def to_dict(self) -> dict[str, Any]:
        role = self.role.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "role": role,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = SetMemberRequestRole(d.pop("role"))




        set_member_request = cls(
            role=role,
        )

        return set_member_request

