from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CompleteNativeBrowserLoginBody")



@_attrs_define
class CompleteNativeBrowserLoginBody:
    """ 
        Attributes:
            state (str):
     """

    state: str





    def to_dict(self) -> dict[str, Any]:
        state = self.state


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "state": state,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state")

        complete_native_browser_login_body = cls(
            state=state,
        )

        return complete_native_browser_login_body

