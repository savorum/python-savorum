from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_resolution_descriptor import ImportResolutionDescriptor





T = TypeVar("T", bound="ImportDiagnosticTarget")



@_attrs_define
class ImportDiagnosticTarget:
    """ 
        Attributes:
            action (str | Unset):
            evidence (str | Unset):
            field (str | Unset):
            object_id (str | Unset):
            preserved (str | Unset):
            resolution (ImportResolutionDescriptor | Unset):
     """

    action: str | Unset = UNSET
    evidence: str | Unset = UNSET
    field: str | Unset = UNSET
    object_id: str | Unset = UNSET
    preserved: str | Unset = UNSET
    resolution: ImportResolutionDescriptor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_resolution_descriptor import ImportResolutionDescriptor # noqa: PLC0415
        action = self.action

        evidence = self.evidence

        field = self.field

        object_id = self.object_id

        preserved = self.preserved

        resolution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if field is not UNSET:
            field_dict["field"] = field
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if preserved is not UNSET:
            field_dict["preserved"] = preserved
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_resolution_descriptor import ImportResolutionDescriptor # noqa: PLC0415
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        evidence = d.pop("evidence", UNSET)

        field = d.pop("field", UNSET)

        object_id = d.pop("object_id", UNSET)

        preserved = d.pop("preserved", UNSET)

        _resolution = d.pop("resolution", UNSET)
        resolution: ImportResolutionDescriptor | Unset
        if isinstance(_resolution,  Unset):
            resolution = UNSET
        else:
            resolution = ImportResolutionDescriptor.from_dict(_resolution)




        import_diagnostic_target = cls(
            action=action,
            evidence=evidence,
            field=field,
            object_id=object_id,
            preserved=preserved,
            resolution=resolution,
        )


        import_diagnostic_target.additional_properties = d
        return import_diagnostic_target

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
