from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="InvitationRegisterRequest")



@_attrs_define
class InvitationRegisterRequest:
    """ 
        Attributes:
            display_name (str):
            login (str):
            password (str):
            token (str):
     """

    display_name: str
    login: str
    password: str
    token: str





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        login = self.login

        password = self.password

        token = self.token


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "display_name": display_name,
            "login": login,
            "password": password,
            "token": token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        login = d.pop("login")

        password = d.pop("password")

        token = d.pop("token")

        invitation_register_request = cls(
            display_name=display_name,
            login=login,
            password=password,
            token=token,
        )

        return invitation_register_request

