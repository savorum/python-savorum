from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MicrowavePower")



@_attrs_define
class MicrowavePower:
    """ 
        Attributes:
            percent (str | Unset):
            text (str | Unset):
            watts (int | Unset):
     """

    percent: str | Unset = UNSET
    text: str | Unset = UNSET
    watts: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        percent = self.percent

        text = self.text

        watts = self.watts


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if percent is not UNSET:
            field_dict["percent"] = percent
        if text is not UNSET:
            field_dict["text"] = text
        if watts is not UNSET:
            field_dict["watts"] = watts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percent = d.pop("percent", UNSET)

        text = d.pop("text", UNSET)

        watts = d.pop("watts", UNSET)

        microwave_power = cls(
            percent=percent,
            text=text,
            watts=watts,
        )

        return microwave_power

