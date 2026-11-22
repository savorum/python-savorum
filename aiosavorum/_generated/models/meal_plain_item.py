from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MealPlainItem")



@_attrs_define
class MealPlainItem:
    """ 
        Attributes:
            name (str):
            id (str | Unset):
            quantity (str | Unset):
     """

    name: str
    id: str | Unset = UNSET
    quantity: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        quantity = self.quantity


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        quantity = d.pop("quantity", UNSET)

        meal_plain_item = cls(
            name=name,
            id=id,
            quantity=quantity,
        )

        return meal_plain_item

