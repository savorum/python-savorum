from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MeasurementResolutionChoice")



@_attrs_define
class MeasurementResolutionChoice:
    """ 
        Attributes:
            convention (str):
            label (str):
            unit_id (str):
            convention_label (str | Unset):
            magnitude (str | Unset):
     """

    convention: str
    label: str
    unit_id: str
    convention_label: str | Unset = UNSET
    magnitude: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        convention = self.convention

        label = self.label

        unit_id = self.unit_id

        convention_label = self.convention_label

        magnitude = self.magnitude


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "convention": convention,
            "label": label,
            "unit_id": unit_id,
        })
        if convention_label is not UNSET:
            field_dict["convention_label"] = convention_label
        if magnitude is not UNSET:
            field_dict["magnitude"] = magnitude

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        convention = d.pop("convention")

        label = d.pop("label")

        unit_id = d.pop("unit_id")

        convention_label = d.pop("convention_label", UNSET)

        magnitude = d.pop("magnitude", UNSET)

        measurement_resolution_choice = cls(
            convention=convention,
            label=label,
            unit_id=unit_id,
            convention_label=convention_label,
            magnitude=magnitude,
        )


        measurement_resolution_choice.additional_properties = d
        return measurement_resolution_choice

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
