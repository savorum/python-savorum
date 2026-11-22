from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Amount")



@_attrs_define
class Amount:
    """ 
        Attributes:
            approximate (bool | Unset):
            max_ (str | Unset):
            min_ (str | Unset):
            value (str | Unset):
     """

    approximate: bool | Unset = UNSET
    max_: str | Unset = UNSET
    min_: str | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        approximate = self.approximate

        max_ = self.max_

        min_ = self.min_

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if approximate is not UNSET:
            field_dict["approximate"] = approximate
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approximate = d.pop("approximate", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        value = d.pop("value", UNSET)

        amount = cls(
            approximate=approximate,
            max_=max_,
            min_=min_,
            value=value,
        )

        return amount

