from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ImportResolutionDescriptor")



@_attrs_define
class ImportResolutionDescriptor:
    """ 
        Attributes:
            authored_form (str):
            candidate_unit_ids (list[str] | None):
            id (str):
            kind (str):
            resolution_key (str):
            source_end (int):
            source_start (int):
     """

    authored_form: str
    candidate_unit_ids: list[str] | None
    id: str
    kind: str
    resolution_key: str
    source_end: int
    source_start: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        authored_form = self.authored_form

        candidate_unit_ids: list[str] | None
        if isinstance(self.candidate_unit_ids, list):
            candidate_unit_ids = self.candidate_unit_ids


        else:
            candidate_unit_ids = self.candidate_unit_ids

        id = self.id

        kind = self.kind

        resolution_key = self.resolution_key

        source_end = self.source_end

        source_start = self.source_start


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "authored_form": authored_form,
            "candidate_unit_ids": candidate_unit_ids,
            "id": id,
            "kind": kind,
            "resolution_key": resolution_key,
            "source_end": source_end,
            "source_start": source_start,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authored_form = d.pop("authored_form")

        def _parse_candidate_unit_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                candidate_unit_ids_type_0 = cast(list[str], data)

                return candidate_unit_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        candidate_unit_ids = _parse_candidate_unit_ids(d.pop("candidate_unit_ids"))


        id = d.pop("id")

        kind = d.pop("kind")

        resolution_key = d.pop("resolution_key")

        source_end = d.pop("source_end")

        source_start = d.pop("source_start")

        import_resolution_descriptor = cls(
            authored_form=authored_form,
            candidate_unit_ids=candidate_unit_ids,
            id=id,
            kind=kind,
            resolution_key=resolution_key,
            source_end=source_end,
            source_start=source_start,
        )


        import_resolution_descriptor.additional_properties = d
        return import_resolution_descriptor

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
