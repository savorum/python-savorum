from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.temperature_purpose_kind import TemperaturePurposeKind
from ..types import UNSET, Unset






T = TypeVar("T", bound="TemperaturePurpose")



@_attrs_define
class TemperaturePurpose:
    """ 
        Attributes:
            kind (TemperaturePurposeKind):
            label (str | Unset):
     """

    kind: TemperaturePurposeKind
    label: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = TemperaturePurposeKind(d.pop("kind"))




        label = d.pop("label", UNSET)

        temperature_purpose = cls(
            kind=kind,
            label=label,
        )

        return temperature_purpose

