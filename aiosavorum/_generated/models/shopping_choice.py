from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ShoppingChoice")



@_attrs_define
class ShoppingChoice:
    """ 
        Attributes:
            id (str):
            name (str):
            note (str):
            quantity (str):
            amount (str | Unset):
            unit (str | Unset):
     """

    id: str
    name: str
    note: str
    quantity: str
    amount: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        note = self.note

        quantity = self.quantity

        amount = self.amount

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "note": note,
            "quantity": quantity,
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        note = d.pop("note")

        quantity = d.pop("quantity")

        amount = d.pop("amount", UNSET)

        unit = d.pop("unit", UNSET)

        shopping_choice = cls(
            id=id,
            name=name,
            note=note,
            quantity=quantity,
            amount=amount,
            unit=unit,
        )


        shopping_choice.additional_properties = d
        return shopping_choice

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
