from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="MeasurementResolutionProfile")



@_attrs_define
class MeasurementResolutionProfile:
    """ 
        Attributes:
            id (str):
            label (str):
            selects (list[str] | None):
            unanswered (list[str] | None):
            unit_registry_version (str):
     """

    id: str
    label: str
    selects: list[str] | None
    unanswered: list[str] | None
    unit_registry_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        selects: list[str] | None
        if isinstance(self.selects, list):
            selects = self.selects


        else:
            selects = self.selects

        unanswered: list[str] | None
        if isinstance(self.unanswered, list):
            unanswered = self.unanswered


        else:
            unanswered = self.unanswered

        unit_registry_version = self.unit_registry_version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "label": label,
            "selects": selects,
            "unanswered": unanswered,
            "unit_registry_version": unit_registry_version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        def _parse_selects(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selects_type_0 = cast(list[str], data)

                return selects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        selects = _parse_selects(d.pop("selects"))


        def _parse_unanswered(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unanswered_type_0 = cast(list[str], data)

                return unanswered_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        unanswered = _parse_unanswered(d.pop("unanswered"))


        unit_registry_version = d.pop("unit_registry_version")

        measurement_resolution_profile = cls(
            id=id,
            label=label,
            selects=selects,
            unanswered=unanswered,
            unit_registry_version=unit_registry_version,
        )


        measurement_resolution_profile.additional_properties = d
        return measurement_resolution_profile

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
