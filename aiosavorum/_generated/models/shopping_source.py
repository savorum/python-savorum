from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="ShoppingSource")



@_attrs_define
class ShoppingSource:
    """ 
        Attributes:
            id (str):
            label (str):
            name (str):
            quantity (str):
            again (str | Unset):
            amount (str | Unset):
            dish_id (str | Unset):
            ingredient_id (str | Unset):
            meal_date (datetime.date | Unset):
            meal_id (str | Unset):
            note (str | Unset):
            recipe_id (str | Unset):
            recipe_revision (int | Unset):
            unit (str | Unset):
     """

    id: str
    label: str
    name: str
    quantity: str
    again: str | Unset = UNSET
    amount: str | Unset = UNSET
    dish_id: str | Unset = UNSET
    ingredient_id: str | Unset = UNSET
    meal_date: datetime.date | Unset = UNSET
    meal_id: str | Unset = UNSET
    note: str | Unset = UNSET
    recipe_id: str | Unset = UNSET
    recipe_revision: int | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        name = self.name

        quantity = self.quantity

        again = self.again

        amount = self.amount

        dish_id = self.dish_id

        ingredient_id = self.ingredient_id

        meal_date: str | Unset = UNSET
        if not isinstance(self.meal_date, Unset):
            meal_date = self.meal_date.isoformat()

        meal_id = self.meal_id

        note = self.note

        recipe_id = self.recipe_id

        recipe_revision = self.recipe_revision

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "label": label,
            "name": name,
            "quantity": quantity,
        })
        if again is not UNSET:
            field_dict["again"] = again
        if amount is not UNSET:
            field_dict["amount"] = amount
        if dish_id is not UNSET:
            field_dict["dish_id"] = dish_id
        if ingredient_id is not UNSET:
            field_dict["ingredient_id"] = ingredient_id
        if meal_date is not UNSET:
            field_dict["meal_date"] = meal_date
        if meal_id is not UNSET:
            field_dict["meal_id"] = meal_id
        if note is not UNSET:
            field_dict["note"] = note
        if recipe_id is not UNSET:
            field_dict["recipe_id"] = recipe_id
        if recipe_revision is not UNSET:
            field_dict["recipe_revision"] = recipe_revision
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        name = d.pop("name")

        quantity = d.pop("quantity")

        again = d.pop("again", UNSET)

        amount = d.pop("amount", UNSET)

        dish_id = d.pop("dish_id", UNSET)

        ingredient_id = d.pop("ingredient_id", UNSET)

        _meal_date = d.pop("meal_date", UNSET)
        meal_date: datetime.date | Unset
        if isinstance(_meal_date,  Unset):
            meal_date = UNSET
        else:
            meal_date = datetime.date.fromisoformat(_meal_date)




        meal_id = d.pop("meal_id", UNSET)

        note = d.pop("note", UNSET)

        recipe_id = d.pop("recipe_id", UNSET)

        recipe_revision = d.pop("recipe_revision", UNSET)

        unit = d.pop("unit", UNSET)

        shopping_source = cls(
            id=id,
            label=label,
            name=name,
            quantity=quantity,
            again=again,
            amount=amount,
            dish_id=dish_id,
            ingredient_id=ingredient_id,
            meal_date=meal_date,
            meal_id=meal_id,
            note=note,
            recipe_id=recipe_id,
            recipe_revision=recipe_revision,
            unit=unit,
        )


        shopping_source.additional_properties = d
        return shopping_source

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
