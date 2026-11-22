from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.assumed_measurement_convention import AssumedMeasurementConvention
  from ..models.import_preview_item import ImportPreviewItem
  from ..models.measurement_resolution_decision import MeasurementResolutionDecision
  from ..models.measurement_resolution_group import MeasurementResolutionGroup
  from ..models.measurement_resolution_profile import MeasurementResolutionProfile





T = TypeVar("T", bound="ImportPreviewResponse")



@_attrs_define
class ImportPreviewResponse:
    """ 
        Attributes:
            expires_at (datetime.datetime):
            id (str):
            items (list[ImportPreviewItem] | None):
            preview_revision (int):
            resolution_decisions (list[MeasurementResolutionDecision] | None):
            resolution_groups (list[MeasurementResolutionGroup] | None):
            resolution_profiles (list[MeasurementResolutionProfile] | None):
            assumed_convention (AssumedMeasurementConvention | Unset):
     """

    expires_at: datetime.datetime
    id: str
    items: list[ImportPreviewItem] | None
    preview_revision: int
    resolution_decisions: list[MeasurementResolutionDecision] | None
    resolution_groups: list[MeasurementResolutionGroup] | None
    resolution_profiles: list[MeasurementResolutionProfile] | None
    assumed_convention: AssumedMeasurementConvention | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.assumed_measurement_convention import AssumedMeasurementConvention # noqa: PLC0415
        from ..models.import_preview_item import ImportPreviewItem # noqa: PLC0415
        from ..models.measurement_resolution_decision import MeasurementResolutionDecision # noqa: PLC0415
        from ..models.measurement_resolution_group import MeasurementResolutionGroup # noqa: PLC0415
        from ..models.measurement_resolution_profile import MeasurementResolutionProfile # noqa: PLC0415
        expires_at = self.expires_at.isoformat()

        id = self.id

        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        preview_revision = self.preview_revision

        resolution_decisions: list[dict[str, Any]] | None
        if isinstance(self.resolution_decisions, list):
            resolution_decisions = []
            for resolution_decisions_type_0_item_data in self.resolution_decisions:
                resolution_decisions_type_0_item = resolution_decisions_type_0_item_data.to_dict()
                resolution_decisions.append(resolution_decisions_type_0_item)


        else:
            resolution_decisions = self.resolution_decisions

        resolution_groups: list[dict[str, Any]] | None
        if isinstance(self.resolution_groups, list):
            resolution_groups = []
            for resolution_groups_type_0_item_data in self.resolution_groups:
                resolution_groups_type_0_item = resolution_groups_type_0_item_data.to_dict()
                resolution_groups.append(resolution_groups_type_0_item)


        else:
            resolution_groups = self.resolution_groups

        resolution_profiles: list[dict[str, Any]] | None
        if isinstance(self.resolution_profiles, list):
            resolution_profiles = []
            for resolution_profiles_type_0_item_data in self.resolution_profiles:
                resolution_profiles_type_0_item = resolution_profiles_type_0_item_data.to_dict()
                resolution_profiles.append(resolution_profiles_type_0_item)


        else:
            resolution_profiles = self.resolution_profiles

        assumed_convention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assumed_convention, Unset):
            assumed_convention = self.assumed_convention.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "expires_at": expires_at,
            "id": id,
            "items": items,
            "preview_revision": preview_revision,
            "resolution_decisions": resolution_decisions,
            "resolution_groups": resolution_groups,
            "resolution_profiles": resolution_profiles,
        })
        if assumed_convention is not UNSET:
            field_dict["assumed_convention"] = assumed_convention

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assumed_measurement_convention import AssumedMeasurementConvention # noqa: PLC0415
        from ..models.import_preview_item import ImportPreviewItem # noqa: PLC0415
        from ..models.measurement_resolution_decision import MeasurementResolutionDecision # noqa: PLC0415
        from ..models.measurement_resolution_group import MeasurementResolutionGroup # noqa: PLC0415
        from ..models.measurement_resolution_profile import MeasurementResolutionProfile # noqa: PLC0415
        d = dict(src_dict)
        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))




        id = d.pop("id")

        def _parse_items(data: object) -> list[ImportPreviewItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = ImportPreviewItem.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportPreviewItem] | None, data)

        items = _parse_items(d.pop("items"))


        preview_revision = d.pop("preview_revision")

        def _parse_resolution_decisions(data: object) -> list[MeasurementResolutionDecision] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolution_decisions_type_0 = []
                _resolution_decisions_type_0 = data
                for resolution_decisions_type_0_item_data in (_resolution_decisions_type_0):
                    resolution_decisions_type_0_item = MeasurementResolutionDecision.from_dict(resolution_decisions_type_0_item_data)



                    resolution_decisions_type_0.append(resolution_decisions_type_0_item)

                return resolution_decisions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionDecision] | None, data)

        resolution_decisions = _parse_resolution_decisions(d.pop("resolution_decisions"))


        def _parse_resolution_groups(data: object) -> list[MeasurementResolutionGroup] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolution_groups_type_0 = []
                _resolution_groups_type_0 = data
                for resolution_groups_type_0_item_data in (_resolution_groups_type_0):
                    resolution_groups_type_0_item = MeasurementResolutionGroup.from_dict(resolution_groups_type_0_item_data)



                    resolution_groups_type_0.append(resolution_groups_type_0_item)

                return resolution_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionGroup] | None, data)

        resolution_groups = _parse_resolution_groups(d.pop("resolution_groups"))


        def _parse_resolution_profiles(data: object) -> list[MeasurementResolutionProfile] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolution_profiles_type_0 = []
                _resolution_profiles_type_0 = data
                for resolution_profiles_type_0_item_data in (_resolution_profiles_type_0):
                    resolution_profiles_type_0_item = MeasurementResolutionProfile.from_dict(resolution_profiles_type_0_item_data)



                    resolution_profiles_type_0.append(resolution_profiles_type_0_item)

                return resolution_profiles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionProfile] | None, data)

        resolution_profiles = _parse_resolution_profiles(d.pop("resolution_profiles"))


        _assumed_convention = d.pop("assumed_convention", UNSET)
        assumed_convention: AssumedMeasurementConvention | Unset
        if isinstance(_assumed_convention,  Unset):
            assumed_convention = UNSET
        else:
            assumed_convention = AssumedMeasurementConvention.from_dict(_assumed_convention)




        import_preview_response = cls(
            expires_at=expires_at,
            id=id,
            items=items,
            preview_revision=preview_revision,
            resolution_decisions=resolution_decisions,
            resolution_groups=resolution_groups,
            resolution_profiles=resolution_profiles,
            assumed_convention=assumed_convention,
        )


        import_preview_response.additional_properties = d
        return import_preview_response

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
