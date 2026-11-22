from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TokenPolicy")



@_attrs_define
class TokenPolicy:
    """ 
        Attributes:
            allow_nonexpiring (bool):
            default_days (int):
            maximum_days (int):
     """

    allow_nonexpiring: bool
    default_days: int
    maximum_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allow_nonexpiring = self.allow_nonexpiring

        default_days = self.default_days

        maximum_days = self.maximum_days


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "allow_nonexpiring": allow_nonexpiring,
            "default_days": default_days,
            "maximum_days": maximum_days,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_nonexpiring = d.pop("allow_nonexpiring")

        default_days = d.pop("default_days")

        maximum_days = d.pop("maximum_days")

        token_policy = cls(
            allow_nonexpiring=allow_nonexpiring,
            default_days=default_days,
            maximum_days=maximum_days,
        )


        token_policy.additional_properties = d
        return token_policy

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
