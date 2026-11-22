from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.print_length import PrintLength





T = TypeVar("T", bound="PrintDimensions")



@_attrs_define
class PrintDimensions:
    """ 
        Attributes:
            height (PrintLength):
            width (PrintLength):
     """

    height: PrintLength
    width: PrintLength
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.print_length import PrintLength # noqa: PLC0415
        height = self.height.to_dict()

        width = self.width.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "height": height,
            "width": width,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.print_length import PrintLength # noqa: PLC0415
        d = dict(src_dict)
        height = PrintLength.from_dict(d.pop("height"))




        width = PrintLength.from_dict(d.pop("width"))




        print_dimensions = cls(
            height=height,
            width=width,
        )


        print_dimensions.additional_properties = d
        return print_dimensions

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
