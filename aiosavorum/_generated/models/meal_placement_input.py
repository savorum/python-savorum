from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.meal_placement_input_meal_type import MealPlacementInputMealType
from ..types import UNSET, Unset






T = TypeVar("T", bound="MealPlacementInput")



@_attrs_define
class MealPlacementInput:
    """ 
        Attributes:
            date (str | Unset):
            meal_type (MealPlacementInputMealType | Unset):
     """

    date: str | Unset = UNSET
    meal_type: MealPlacementInputMealType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        date = self.date

        meal_type: str | Unset = UNSET
        if not isinstance(self.meal_type, Unset):
            meal_type = self.meal_type.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if meal_type is not UNSET:
            field_dict["meal_type"] = meal_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        _meal_type = d.pop("meal_type", UNSET)
        meal_type: MealPlacementInputMealType | Unset
        if isinstance(_meal_type,  Unset):
            meal_type = UNSET
        else:
            meal_type = MealPlacementInputMealType(_meal_type)




        meal_placement_input = cls(
            date=date,
            meal_type=meal_type,
        )

        return meal_placement_input

