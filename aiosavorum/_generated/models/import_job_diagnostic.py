from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_job_diagnostic_class import ImportJobDiagnosticClass
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_diagnostic_target import ImportDiagnosticTarget





T = TypeVar("T", bound="ImportJobDiagnostic")



@_attrs_define
class ImportJobDiagnostic:
    """ 
        Attributes:
            area (str):
            class_ (ImportJobDiagnosticClass):
            code (str):
            count (int):
            message (str):
            targets (list[ImportDiagnosticTarget] | None | Unset):
     """

    area: str
    class_: ImportJobDiagnosticClass
    code: str
    count: int
    message: str
    targets: list[ImportDiagnosticTarget] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_diagnostic_target import ImportDiagnosticTarget # noqa: PLC0415
        area = self.area

        class_ = self.class_.value

        code = self.code

        count = self.count

        message = self.message

        targets: list[dict[str, Any]] | None | Unset
        if isinstance(self.targets, Unset):
            targets = UNSET
        elif isinstance(self.targets, list):
            targets = []
            for targets_type_0_item_data in self.targets:
                targets_type_0_item = targets_type_0_item_data.to_dict()
                targets.append(targets_type_0_item)


        else:
            targets = self.targets


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "area": area,
            "class": class_,
            "code": code,
            "count": count,
            "message": message,
        })
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_diagnostic_target import ImportDiagnosticTarget # noqa: PLC0415
        d = dict(src_dict)
        area = d.pop("area")

        class_ = ImportJobDiagnosticClass(d.pop("class"))




        code = d.pop("code")

        count = d.pop("count")

        message = d.pop("message")

        def _parse_targets(data: object) -> list[ImportDiagnosticTarget] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                targets_type_0 = []
                _targets_type_0 = data
                for targets_type_0_item_data in (_targets_type_0):
                    targets_type_0_item = ImportDiagnosticTarget.from_dict(targets_type_0_item_data)



                    targets_type_0.append(targets_type_0_item)

                return targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportDiagnosticTarget] | None | Unset, data)

        targets = _parse_targets(d.pop("targets", UNSET))


        import_job_diagnostic = cls(
            area=area,
            class_=class_,
            code=code,
            count=count,
            message=message,
            targets=targets,
        )


        import_job_diagnostic.additional_properties = d
        return import_job_diagnostic

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
