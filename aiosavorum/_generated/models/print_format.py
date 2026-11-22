from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.print_dimensions import PrintDimensions
  from ..models.print_length import PrintLength





T = TypeVar("T", bound="PrintFormat")



@_attrs_define
class PrintFormat:
    """ 
        Attributes:
            family (str):
            height (PrintLength):
            size (str):
            width (PrintLength):
            card (PrintDimensions | Unset):
     """

    family: str
    height: PrintLength
    size: str
    width: PrintLength
    card: PrintDimensions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.print_dimensions import PrintDimensions # noqa: PLC0415
        from ..models.print_length import PrintLength # noqa: PLC0415
        family = self.family

        height = self.height.to_dict()

        size = self.size

        width = self.width.to_dict()

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "family": family,
            "height": height,
            "size": size,
            "width": width,
        })
        if card is not UNSET:
            field_dict["card"] = card

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.print_dimensions import PrintDimensions # noqa: PLC0415
        from ..models.print_length import PrintLength # noqa: PLC0415
        d = dict(src_dict)
        family = d.pop("family")

        height = PrintLength.from_dict(d.pop("height"))




        size = d.pop("size")

        width = PrintLength.from_dict(d.pop("width"))




        _card = d.pop("card", UNSET)
        card: PrintDimensions | Unset
        if isinstance(_card,  Unset):
            card = UNSET
        else:
            card = PrintDimensions.from_dict(_card)




        print_format = cls(
            family=family,
            height=height,
            size=size,
            width=width,
            card=card,
        )


        print_format.additional_properties = d
        return print_format

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
