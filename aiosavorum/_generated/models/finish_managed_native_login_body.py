from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FinishManagedNativeLoginBody")



@_attrs_define
class FinishManagedNativeLoginBody:
    """ 
        Attributes:
            code_verifier (str):
            grant (str):
     """

    code_verifier: str
    grant: str





    def to_dict(self) -> dict[str, Any]:
        code_verifier = self.code_verifier

        grant = self.grant


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code_verifier": code_verifier,
            "grant": grant,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code_verifier = d.pop("code_verifier")

        grant = d.pop("grant")

        finish_managed_native_login_body = cls(
            code_verifier=code_verifier,
            grant=grant,
        )

        return finish_managed_native_login_body

