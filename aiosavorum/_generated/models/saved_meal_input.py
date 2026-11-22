from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.meal_dish import MealDish





T = TypeVar("T", bound="SavedMealInput")



@_attrs_define
class SavedMealInput:
    """ 
        Attributes:
            dishes (list[MealDish] | None):
            name (str):
            notes (str | Unset):
     """

    dishes: list[MealDish] | None
    name: str
    notes: str | Unset = UNSET





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

        name = self.name

        notes = self.notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "dishes": dishes,
            "name": name,
        })
        if notes is not UNSET:
            field_dict["notes"] = notes

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


        name = d.pop("name")

        notes = d.pop("notes", UNSET)

        saved_meal_input = cls(
            dishes=dishes,
            name=name,
            notes=notes,
        )

        return saved_meal_input

