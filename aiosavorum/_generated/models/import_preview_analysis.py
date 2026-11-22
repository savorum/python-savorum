from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_preview_analysis_status import ImportPreviewAnalysisStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.import_preview_match import ImportPreviewMatch





T = TypeVar("T", bound="ImportPreviewAnalysis")



@_attrs_define
class ImportPreviewAnalysis:
    """ 
        Attributes:
            matches (list[ImportPreviewMatch] | None):
            status (ImportPreviewAnalysisStatus):
     """

    matches: list[ImportPreviewMatch] | None
    status: ImportPreviewAnalysisStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_preview_match import ImportPreviewMatch # noqa: PLC0415
        matches: list[dict[str, Any]] | None
        if isinstance(self.matches, list):
            matches = []
            for matches_type_0_item_data in self.matches:
                matches_type_0_item = matches_type_0_item_data.to_dict()
                matches.append(matches_type_0_item)


        else:
            matches = self.matches

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "matches": matches,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_preview_match import ImportPreviewMatch # noqa: PLC0415
        d = dict(src_dict)
        def _parse_matches(data: object) -> list[ImportPreviewMatch] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                matches_type_0 = []
                _matches_type_0 = data
                for matches_type_0_item_data in (_matches_type_0):
                    matches_type_0_item = ImportPreviewMatch.from_dict(matches_type_0_item_data)



                    matches_type_0.append(matches_type_0_item)

                return matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportPreviewMatch] | None, data)

        matches = _parse_matches(d.pop("matches"))


        status = ImportPreviewAnalysisStatus(d.pop("status"))




        import_preview_analysis = cls(
            matches=matches,
            status=status,
        )


        import_preview_analysis.additional_properties = d
        return import_preview_analysis

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
