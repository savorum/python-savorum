from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.meal_dish import MealDish





T = TypeVar("T", bound="SavedMeal")



@_attrs_define
class SavedMeal:
    """ 
        Attributes:
            created_at (datetime.datetime):
            dishes (list[MealDish] | None):
            id (str):
            name (str):
            revision (int):
            updated_at (datetime.datetime):
            notes (str | Unset):
     """

    created_at: datetime.datetime
    dishes: list[MealDish] | None
    id: str
    name: str
    revision: int
    updated_at: datetime.datetime
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.meal_dish import MealDish # noqa: PLC0415
        created_at = self.created_at.isoformat()

        dishes: list[dict[str, Any]] | None
        if isinstance(self.dishes, list):
            dishes = []
            for dishes_type_0_item_data in self.dishes:
                dishes_type_0_item = dishes_type_0_item_data.to_dict()
                dishes.append(dishes_type_0_item)


        else:
            dishes = self.dishes

        id = self.id

        name = self.name

        revision = self.revision

        updated_at = self.updated_at.isoformat()

        notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "dishes": dishes,
            "id": id,
            "name": name,
            "revision": revision,
            "updated_at": updated_at,
        })
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meal_dish import MealDish # noqa: PLC0415
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




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


        id = d.pop("id")

        name = d.pop("name")

        revision = d.pop("revision")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        notes = d.pop("notes", UNSET)

        saved_meal = cls(
            created_at=created_at,
            dishes=dishes,
            id=id,
            name=name,
            revision=revision,
            updated_at=updated_at,
            notes=notes,
        )


        saved_meal.additional_properties = d
        return saved_meal

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
