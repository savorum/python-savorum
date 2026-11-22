from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PasswordRequest")



@_attrs_define
class PasswordRequest:
    """ 
        Attributes:
            current_password (str):
            new_password (str):
     """

    current_password: str
    new_password: str





    def to_dict(self) -> dict[str, Any]:
        current_password = self.current_password

        new_password = self.new_password


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "current_password": current_password,
            "new_password": new_password,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_password = d.pop("current_password")

        new_password = d.pop("new_password")

        password_request = cls(
            current_password=current_password,
            new_password=new_password,
        )

        return password_request

