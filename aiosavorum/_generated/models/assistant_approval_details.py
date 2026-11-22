from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AssistantApprovalDetails")



@_attrs_define
class AssistantApprovalDetails:
    """ 
        Attributes:
            client_name (str):
            client_origin (str):
            reauth_required (bool):
            remember_days (int):
            scope (str):
            user_code (str):
            verification_required (bool):
     """

    client_name: str
    client_origin: str
    reauth_required: bool
    remember_days: int
    scope: str
    user_code: str
    verification_required: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        client_name = self.client_name

        client_origin = self.client_origin

        reauth_required = self.reauth_required

        remember_days = self.remember_days

        scope = self.scope

        user_code = self.user_code

        verification_required = self.verification_required


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "client_name": client_name,
            "client_origin": client_origin,
            "reauth_required": reauth_required,
            "remember_days": remember_days,
            "scope": scope,
            "user_code": user_code,
            "verification_required": verification_required,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_name = d.pop("client_name")

        client_origin = d.pop("client_origin")

        reauth_required = d.pop("reauth_required")

        remember_days = d.pop("remember_days")

        scope = d.pop("scope")

        user_code = d.pop("user_code")

        verification_required = d.pop("verification_required")

        assistant_approval_details = cls(
            client_name=client_name,
            client_origin=client_origin,
            reauth_required=reauth_required,
            remember_days=remember_days,
            scope=scope,
            user_code=user_code,
            verification_required=verification_required,
        )


        assistant_approval_details.additional_properties = d
        return assistant_approval_details

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
