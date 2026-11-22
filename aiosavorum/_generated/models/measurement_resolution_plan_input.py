from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.measurement_resolution_interpretation_input import MeasurementResolutionInterpretationInput





T = TypeVar("T", bound="MeasurementResolutionPlanInput")



@_attrs_define
class MeasurementResolutionPlanInput:
    """ 
        Attributes:
            expected_preview_revision (int):
            interpretation (MeasurementResolutionInterpretationInput):
            excluded_item_ids (list[str] | None | Unset):
            excluded_occurrence_ids (list[str] | None | Unset):
            resolution_group_ids (list[str] | None | Unset):
     """

    expected_preview_revision: int
    interpretation: MeasurementResolutionInterpretationInput
    excluded_item_ids: list[str] | None | Unset = UNSET
    excluded_occurrence_ids: list[str] | None | Unset = UNSET
    resolution_group_ids: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_resolution_interpretation_input import MeasurementResolutionInterpretationInput # noqa: PLC0415
        expected_preview_revision = self.expected_preview_revision

        interpretation = self.interpretation.to_dict()

        excluded_item_ids: list[str] | None | Unset
        if isinstance(self.excluded_item_ids, Unset):
            excluded_item_ids = UNSET
        elif isinstance(self.excluded_item_ids, list):
            excluded_item_ids = self.excluded_item_ids


        else:
            excluded_item_ids = self.excluded_item_ids

        excluded_occurrence_ids: list[str] | None | Unset
        if isinstance(self.excluded_occurrence_ids, Unset):
            excluded_occurrence_ids = UNSET
        elif isinstance(self.excluded_occurrence_ids, list):
            excluded_occurrence_ids = self.excluded_occurrence_ids


        else:
            excluded_occurrence_ids = self.excluded_occurrence_ids

        resolution_group_ids: list[str] | None | Unset
        if isinstance(self.resolution_group_ids, Unset):
            resolution_group_ids = UNSET
        elif isinstance(self.resolution_group_ids, list):
            resolution_group_ids = self.resolution_group_ids


        else:
            resolution_group_ids = self.resolution_group_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expected_preview_revision": expected_preview_revision,
            "interpretation": interpretation,
        })
        if excluded_item_ids is not UNSET:
            field_dict["excluded_item_ids"] = excluded_item_ids
        if excluded_occurrence_ids is not UNSET:
            field_dict["excluded_occurrence_ids"] = excluded_occurrence_ids
        if resolution_group_ids is not UNSET:
            field_dict["resolution_group_ids"] = resolution_group_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_resolution_interpretation_input import MeasurementResolutionInterpretationInput # noqa: PLC0415
        d = dict(src_dict)
        expected_preview_revision = d.pop("expected_preview_revision")

        interpretation = MeasurementResolutionInterpretationInput.from_dict(d.pop("interpretation"))




        def _parse_excluded_item_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_item_ids_type_0 = cast(list[str], data)

                return excluded_item_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        excluded_item_ids = _parse_excluded_item_ids(d.pop("excluded_item_ids", UNSET))


        def _parse_excluded_occurrence_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_occurrence_ids_type_0 = cast(list[str], data)

                return excluded_occurrence_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        excluded_occurrence_ids = _parse_excluded_occurrence_ids(d.pop("excluded_occurrence_ids", UNSET))


        def _parse_resolution_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolution_group_ids_type_0 = cast(list[str], data)

                return resolution_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        resolution_group_ids = _parse_resolution_group_ids(d.pop("resolution_group_ids", UNSET))


        measurement_resolution_plan_input = cls(
            expected_preview_revision=expected_preview_revision,
            interpretation=interpretation,
            excluded_item_ids=excluded_item_ids,
            excluded_occurrence_ids=excluded_occurrence_ids,
            resolution_group_ids=resolution_group_ids,
        )

        return measurement_resolution_plan_input

