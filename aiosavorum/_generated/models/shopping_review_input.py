from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shopping_portion import ShoppingPortion





T = TypeVar("T", bound="ShoppingReviewInput")



@_attrs_define
class ShoppingReviewInput:
    """ 
        Attributes:
            again (str | Unset):
            meal_ids (list[str] | None | Unset):
            portions (list[ShoppingPortion] | None | Unset):
            refresh_recipes (bool | Unset):
     """

    again: str | Unset = UNSET
    meal_ids: list[str] | None | Unset = UNSET
    portions: list[ShoppingPortion] | None | Unset = UNSET
    refresh_recipes: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.shopping_portion import ShoppingPortion # noqa: PLC0415
        again = self.again

        meal_ids: list[str] | None | Unset
        if isinstance(self.meal_ids, Unset):
            meal_ids = UNSET
        elif isinstance(self.meal_ids, list):
            meal_ids = self.meal_ids


        else:
            meal_ids = self.meal_ids

        portions: list[dict[str, Any]] | None | Unset
        if isinstance(self.portions, Unset):
            portions = UNSET
        elif isinstance(self.portions, list):
            portions = []
            for portions_type_0_item_data in self.portions:
                portions_type_0_item = portions_type_0_item_data.to_dict()
                portions.append(portions_type_0_item)


        else:
            portions = self.portions

        refresh_recipes = self.refresh_recipes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if again is not UNSET:
            field_dict["again"] = again
        if meal_ids is not UNSET:
            field_dict["meal_ids"] = meal_ids
        if portions is not UNSET:
            field_dict["portions"] = portions
        if refresh_recipes is not UNSET:
            field_dict["refresh_recipes"] = refresh_recipes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shopping_portion import ShoppingPortion # noqa: PLC0415
        d = dict(src_dict)
        again = d.pop("again", UNSET)

        def _parse_meal_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                meal_ids_type_0 = cast(list[str], data)

                return meal_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        meal_ids = _parse_meal_ids(d.pop("meal_ids", UNSET))


        def _parse_portions(data: object) -> list[ShoppingPortion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                portions_type_0 = []
                _portions_type_0 = data
                for portions_type_0_item_data in (_portions_type_0):
                    portions_type_0_item = ShoppingPortion.from_dict(portions_type_0_item_data)



                    portions_type_0.append(portions_type_0_item)

                return portions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShoppingPortion] | None | Unset, data)

        portions = _parse_portions(d.pop("portions", UNSET))


        refresh_recipes = d.pop("refresh_recipes", UNSET)

        shopping_review_input = cls(
            again=again,
            meal_ids=meal_ids,
            portions=portions,
            refresh_recipes=refresh_recipes,
        )

        return shopping_review_input

