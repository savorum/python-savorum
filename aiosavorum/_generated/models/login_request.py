from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="LoginRequest")



@_attrs_define
class LoginRequest:
    """ 
        Attributes:
            login (str):
            password (str):
     """

    login: str
    password: str





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        password = self.password


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "login": login,
            "password": password,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login")

        password = d.pop("password")

        login_request = cls(
            login=login,
            password=password,
        )

        return login_request

