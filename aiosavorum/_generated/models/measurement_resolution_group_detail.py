from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.measurement_resolution_group import MeasurementResolutionGroup
  from ..models.measurement_resolution_occurrence import MeasurementResolutionOccurrence





T = TypeVar("T", bound="MeasurementResolutionGroupDetail")



@_attrs_define
class MeasurementResolutionGroupDetail:
    """ 
        Attributes:
            group (MeasurementResolutionGroup):
            occurrences (list[MeasurementResolutionOccurrence] | None):
     """

    group: MeasurementResolutionGroup
    occurrences: list[MeasurementResolutionOccurrence] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_resolution_group import MeasurementResolutionGroup # noqa: PLC0415
        from ..models.measurement_resolution_occurrence import MeasurementResolutionOccurrence # noqa: PLC0415
        group = self.group.to_dict()

        occurrences: list[dict[str, Any]] | None
        if isinstance(self.occurrences, list):
            occurrences = []
            for occurrences_type_0_item_data in self.occurrences:
                occurrences_type_0_item = occurrences_type_0_item_data.to_dict()
                occurrences.append(occurrences_type_0_item)


        else:
            occurrences = self.occurrences


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "group": group,
            "occurrences": occurrences,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_resolution_group import MeasurementResolutionGroup # noqa: PLC0415
        from ..models.measurement_resolution_occurrence import MeasurementResolutionOccurrence # noqa: PLC0415
        d = dict(src_dict)
        group = MeasurementResolutionGroup.from_dict(d.pop("group"))




        def _parse_occurrences(data: object) -> list[MeasurementResolutionOccurrence] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                occurrences_type_0 = []
                _occurrences_type_0 = data
                for occurrences_type_0_item_data in (_occurrences_type_0):
                    occurrences_type_0_item = MeasurementResolutionOccurrence.from_dict(occurrences_type_0_item_data)



                    occurrences_type_0.append(occurrences_type_0_item)

                return occurrences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionOccurrence] | None, data)

        occurrences = _parse_occurrences(d.pop("occurrences"))


        measurement_resolution_group_detail = cls(
            group=group,
            occurrences=occurrences,
        )


        measurement_resolution_group_detail.additional_properties = d
        return measurement_resolution_group_detail

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
