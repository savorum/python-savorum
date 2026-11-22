from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BeginProviderLoginBody")



@_attrs_define
class BeginProviderLoginBody:
    """ 
        Attributes:
            invitation_token (str | Unset):
            link (bool | Unset): Requires a browser session authenticated within the last five minutes and CSRF proof;
                callback rechecks session validity and freshness.
            login (str | Unset):
            password (str | Unset):
     """

    invitation_token: str | Unset = UNSET
    link: bool | Unset = UNSET
    login: str | Unset = UNSET
    password: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        invitation_token = self.invitation_token

        link = self.link

        login = self.login

        password = self.password


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if invitation_token is not UNSET:
            field_dict["invitation_token"] = invitation_token
        if link is not UNSET:
            field_dict["link"] = link
        if login is not UNSET:
            field_dict["login"] = login
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invitation_token = d.pop("invitation_token", UNSET)

        link = d.pop("link", UNSET)

        login = d.pop("login", UNSET)

        password = d.pop("password", UNSET)

        begin_provider_login_body = cls(
            invitation_token=invitation_token,
            link=link,
            login=login,
            password=password,
        )

        return begin_provider_login_body

