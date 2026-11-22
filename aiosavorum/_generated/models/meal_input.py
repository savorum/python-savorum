from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.meal_input_meal_type import MealInputMealType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.meal_dish import MealDish





T = TypeVar("T", bound="MealInput")



@_attrs_define
class MealInput:
    """ 
        Attributes:
            dishes (list[MealDish] | None):
            date (str | Unset):
            meal_type (MealInputMealType | Unset):
            name (str | Unset):
            notes (str | Unset):
            skipped (bool | Unset):
     """

    dishes: list[MealDish] | None
    date: str | Unset = UNSET
    meal_type: MealInputMealType | Unset = UNSET
    name: str | Unset = UNSET
    notes: str | Unset = UNSET
    skipped: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.meal_dish import MealDish # noqa: PLC0415
        dishes: list[dict[str, Any]] | None
        if isinstance(self.dishes, list):
            dishes = []
            for dishes_type_0_item_data in self.dishes:
                dishes_type_0_item = dishes_type_0_item_data.to_dict()
                dishes.append(dishes_type_0_item)


        else:
            dishes = self.dishes

        date = self.date

        meal_type: str | Unset = UNSET
        if not isinstance(self.meal_type, Unset):
            meal_type = self.meal_type.value


        name = self.name

        notes = self.notes

        skipped = self.skipped


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "dishes": dishes,
        })
        if date is not UNSET:
            field_dict["date"] = date
        if meal_type is not UNSET:
            field_dict["meal_type"] = meal_type
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meal_dish import MealDish # noqa: PLC0415
        d = dict(src_dict)
        def _parse_dishes(data: object) -> list[MealDish] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dishes_type_0 = []
                _dishes_type_0 = data
                for dishes_type_0_item_data in (_dishes_type_0):
                    dishes_type_0_item = MealDish.from_dict(dishes_type_0_item_data)



                    dishes_type_0.append(dishes_type_0_item)

                return dishes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MealDish] | None, data)

        dishes = _parse_dishes(d.pop("dishes"))


        date = d.pop("date", UNSET)

        _meal_type = d.pop("meal_type", UNSET)
        meal_type: MealInputMealType | Unset
        if isinstance(_meal_type,  Unset):
            meal_type = UNSET
        else:
            meal_type = MealInputMealType(_meal_type)




        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        skipped = d.pop("skipped", UNSET)

        meal_input = cls(
            dishes=dishes,
            date=date,
            meal_type=meal_type,
            name=name,
            notes=notes,
            skipped=skipped,
        )

        return meal_input

