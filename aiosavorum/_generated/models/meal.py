from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.meal_meal_type import MealMealType
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.meal_dish import MealDish





T = TypeVar("T", bound="Meal")



@_attrs_define
class Meal:
    """ 
        Attributes:
            created_at (datetime.datetime):
            dishes (list[MealDish] | None):
            display_title (str):
            id (str):
            revision (int):
            skipped (bool):
            updated_at (datetime.datetime):
            created_by (str | Unset):
            created_by_name (str | Unset):
            date (str | Unset):
            meal_type (MealMealType | Unset):
            name (str | Unset):
            notes (str | Unset):
            updated_by (str | Unset):
            updated_by_name (str | Unset):
     """

    created_at: datetime.datetime
    dishes: list[MealDish] | None
    display_title: str
    id: str
    revision: int
    skipped: bool
    updated_at: datetime.datetime
    created_by: str | Unset = UNSET
    created_by_name: str | Unset = UNSET
    date: str | Unset = UNSET
    meal_type: MealMealType | Unset = UNSET
    name: str | Unset = UNSET
    notes: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    updated_by_name: str | Unset = UNSET
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

        display_title = self.display_title

        id = self.id

        revision = self.revision

        skipped = self.skipped

        updated_at = self.updated_at.isoformat()

        created_by = self.created_by

        created_by_name = self.created_by_name

        date = self.date

        meal_type: str | Unset = UNSET
        if not isinstance(self.meal_type, Unset):
            meal_type = self.meal_type.value


        name = self.name

        notes = self.notes

        updated_by = self.updated_by

        updated_by_name = self.updated_by_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "dishes": dishes,
            "display_title": display_title,
            "id": id,
            "revision": revision,
            "skipped": skipped,
            "updated_at": updated_at,
        })
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_name is not UNSET:
            field_dict["created_by_name"] = created_by_name
        if date is not UNSET:
            field_dict["date"] = date
        if meal_type is not UNSET:
            field_dict["meal_type"] = meal_type
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if updated_by_name is not UNSET:
            field_dict["updated_by_name"] = updated_by_name

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


        display_title = d.pop("display_title")

        id = d.pop("id")

        revision = d.pop("revision")

        skipped = d.pop("skipped")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        created_by = d.pop("created_by", UNSET)

        created_by_name = d.pop("created_by_name", UNSET)

        date = d.pop("date", UNSET)

        _meal_type = d.pop("meal_type", UNSET)
        meal_type: MealMealType | Unset
        if isinstance(_meal_type,  Unset):
            meal_type = UNSET
        else:
            meal_type = MealMealType(_meal_type)




        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        updated_by = d.pop("updated_by", UNSET)

        updated_by_name = d.pop("updated_by_name", UNSET)

        meal = cls(
            created_at=created_at,
            dishes=dishes,
            display_title=display_title,
            id=id,
            revision=revision,
            skipped=skipped,
            updated_at=updated_at,
            created_by=created_by,
            created_by_name=created_by_name,
            date=date,
            meal_type=meal_type,
            name=name,
            notes=notes,
            updated_by=updated_by,
            updated_by_name=updated_by_name,
        )


        meal.additional_properties = d
        return meal

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
