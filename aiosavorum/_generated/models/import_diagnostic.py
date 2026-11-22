from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ImportDiagnostic")



@_attrs_define
class ImportDiagnostic:
    """ 
        Attributes:
            class_ (str):
            code (str):
            count (int):
            message (str):
            area (str | Unset):
     """

    class_: str
    code: str
    count: int
    message: str
    area: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        class_ = self.class_

        code = self.code

        count = self.count

        message = self.message

        area = self.area


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "class": class_,
            "code": code,
            "count": count,
            "message": message,
        })
        if area is not UNSET:
            field_dict["area"] = area

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        class_ = d.pop("class")

        code = d.pop("code")

        count = d.pop("count")

        message = d.pop("message")

        area = d.pop("area", UNSET)

        import_diagnostic = cls(
            class_=class_,
            code=code,
            count=count,
            message=message,
            area=area,
        )


        import_diagnostic.additional_properties = d
        return import_diagnostic

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
