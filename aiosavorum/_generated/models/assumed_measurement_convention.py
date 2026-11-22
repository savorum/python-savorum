from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.assumed_measurement_convention_convention import AssumedMeasurementConventionConvention






T = TypeVar("T", bound="AssumedMeasurementConvention")



@_attrs_define
class AssumedMeasurementConvention:
    """ 
        Attributes:
            convention (AssumedMeasurementConventionConvention):
            host (str):
            label (str):
            plan_id (str):
            revertible (bool):
     """

    convention: AssumedMeasurementConventionConvention
    host: str
    label: str
    plan_id: str
    revertible: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        convention = self.convention.value

        host = self.host

        label = self.label

        plan_id = self.plan_id

        revertible = self.revertible


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "convention": convention,
            "host": host,
            "label": label,
            "plan_id": plan_id,
            "revertible": revertible,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        convention = AssumedMeasurementConventionConvention(d.pop("convention"))




        host = d.pop("host")

        label = d.pop("label")

        plan_id = d.pop("plan_id")

        revertible = d.pop("revertible")

        assumed_measurement_convention = cls(
            convention=convention,
            host=host,
            label=label,
            plan_id=plan_id,
            revertible=revertible,
        )


        assumed_measurement_convention.additional_properties = d
        return assumed_measurement_convention

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
