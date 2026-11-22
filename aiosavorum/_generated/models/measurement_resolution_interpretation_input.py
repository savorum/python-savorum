from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.measurement_resolution_interpretation_input_convention import MeasurementResolutionInterpretationInputConvention
from ..models.measurement_resolution_interpretation_input_kind import MeasurementResolutionInterpretationInputKind
from ..types import UNSET, Unset






T = TypeVar("T", bound="MeasurementResolutionInterpretationInput")



@_attrs_define
class MeasurementResolutionInterpretationInput:
    """ 
        Attributes:
            kind (MeasurementResolutionInterpretationInputKind):
            convention (MeasurementResolutionInterpretationInputConvention | Unset):
            unit_id (str | Unset):
     """

    kind: MeasurementResolutionInterpretationInputKind
    convention: MeasurementResolutionInterpretationInputConvention | Unset = UNSET
    unit_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        convention: str | Unset = UNSET
        if not isinstance(self.convention, Unset):
            convention = self.convention.value


        unit_id = self.unit_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })
        if convention is not UNSET:
            field_dict["convention"] = convention
        if unit_id is not UNSET:
            field_dict["unit_id"] = unit_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = MeasurementResolutionInterpretationInputKind(d.pop("kind"))




        _convention = d.pop("convention", UNSET)
        convention: MeasurementResolutionInterpretationInputConvention | Unset
        if isinstance(_convention,  Unset):
            convention = UNSET
        else:
            convention = MeasurementResolutionInterpretationInputConvention(_convention)




        unit_id = d.pop("unit_id", UNSET)

        measurement_resolution_interpretation_input = cls(
            kind=kind,
            convention=convention,
            unit_id=unit_id,
        )

        return measurement_resolution_interpretation_input

