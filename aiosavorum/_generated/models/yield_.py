from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.quantity import Quantity





T = TypeVar("T", bound="Yield")



@_attrs_define
class Yield:
    """ 
        Attributes:
            label (str | Unset):
            quantity (Quantity | Unset):
            text (str | Unset):
     """

    label: str | Unset = UNSET
    quantity: Quantity | Unset = UNSET
    text: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.quantity import Quantity # noqa: PLC0415
        label = self.label

        quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quantity, Unset):
            quantity = self.quantity.to_dict()

        text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if label is not UNSET:
            field_dict["label"] = label
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quantity import Quantity # noqa: PLC0415
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        _quantity = d.pop("quantity", UNSET)
        quantity: Quantity | Unset
        if isinstance(_quantity,  Unset):
            quantity = UNSET
        else:
            quantity = Quantity.from_dict(_quantity)




        text = d.pop("text", UNSET)

        yield_ = cls(
            label=label,
            quantity=quantity,
            text=text,
        )

        return yield_

