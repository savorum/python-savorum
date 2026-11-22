from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateUserRequest")



@_attrs_define
class UpdateUserRequest:
    """ 
        Attributes:
            disabled (bool | Unset):
            password (str | Unset):
     """

    disabled: bool | Unset = UNSET
    password: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        disabled = self.disabled

        password = self.password


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disabled = d.pop("disabled", UNSET)

        password = d.pop("password", UNSET)

        update_user_request = cls(
            disabled=disabled,
            password=password,
        )

        return update_user_request

