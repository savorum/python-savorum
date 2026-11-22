from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FinishNativeProviderLoginBody")



@_attrs_define
class FinishNativeProviderLoginBody:
    """ 
        Attributes:
            code (str): The one-time code from the return target. It expires after one minute and is consumed by the first
                attempt.
            code_verifier (str): The PKCE verifier: 43 to 128 unreserved characters.
            redirect_uri (str): The return target used to begin the sign-in.
     """

    code: str
    code_verifier: str
    redirect_uri: str





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        code_verifier = self.code_verifier

        redirect_uri = self.redirect_uri


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "code_verifier": code_verifier,
            "redirect_uri": redirect_uri,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        code_verifier = d.pop("code_verifier")

        redirect_uri = d.pop("redirect_uri")

        finish_native_provider_login_body = cls(
            code=code,
            code_verifier=code_verifier,
            redirect_uri=redirect_uri,
        )

        return finish_native_provider_login_body

