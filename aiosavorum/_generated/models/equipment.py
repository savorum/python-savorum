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





T = TypeVar("T", bound="Equipment")



@_attrs_define
class Equipment:
    """ 
        Attributes:
            name (str): Authored equipment description; not a normalized registry identity
            note (str | Unset):
            quantity (Quantity | Unset):
     """

    name: str
    note: str | Unset = UNSET
    quantity: Quantity | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.quantity import Quantity # noqa: PLC0415
        name = self.name

        note = self.note

        quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quantity, Unset):
            quantity = self.quantity.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if note is not UNSET:
            field_dict["note"] = note
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quantity import Quantity # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        note = d.pop("note", UNSET)

        _quantity = d.pop("quantity", UNSET)
        quantity: Quantity | Unset
        if isinstance(_quantity,  Unset):
            quantity = UNSET
        else:
            quantity = Quantity.from_dict(_quantity)




        equipment = cls(
            name=name,
            note=note,
            quantity=quantity,
        )

        return equipment

