from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invitation_create_request_role import InvitationCreateRequestRole
from ..types import UNSET, Unset






T = TypeVar("T", bound="InvitationCreateRequest")



@_attrs_define
class InvitationCreateRequest:
    """ 
        Attributes:
            role (InvitationCreateRequestRole):
            days (int | Unset):
            hint (str | Unset):
     """

    role: InvitationCreateRequestRole
    days: int | Unset = UNSET
    hint: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        days = self.days

        hint = self.hint


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "role": role,
        })
        if days is not UNSET:
            field_dict["days"] = days
        if hint is not UNSET:
            field_dict["hint"] = hint

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = InvitationCreateRequestRole(d.pop("role"))




        days = d.pop("days", UNSET)

        hint = d.pop("hint", UNSET)

        invitation_create_request = cls(
            role=role,
            days=days,
            hint=hint,
        )

        return invitation_create_request

