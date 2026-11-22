from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ingredient import Ingredient





T = TypeVar("T", bound="IngredientSection")



@_attrs_define
class IngredientSection:
    """ 
        Attributes:
            id (str):
            ingredients (list[Ingredient] | None):
            title (str | Unset):
     """

    id: str
    ingredients: list[Ingredient] | None
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.ingredient import Ingredient # noqa: PLC0415
        id = self.id

        ingredients: list[dict[str, Any]] | None
        if isinstance(self.ingredients, list):
            ingredients = []
            for ingredients_type_0_item_data in self.ingredients:
                ingredients_type_0_item = ingredients_type_0_item_data.to_dict()
                ingredients.append(ingredients_type_0_item)


        else:
            ingredients = self.ingredients

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ingredients": ingredients,
        })
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingredient import Ingredient # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_ingredients(data: object) -> list[Ingredient] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ingredients_type_0 = []
                _ingredients_type_0 = data
                for ingredients_type_0_item_data in (_ingredients_type_0):
                    ingredients_type_0_item = Ingredient.from_dict(ingredients_type_0_item_data)



                    ingredients_type_0.append(ingredients_type_0_item)

                return ingredients_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ingredient] | None, data)

        ingredients = _parse_ingredients(d.pop("ingredients"))


        title = d.pop("title", UNSET)

        ingredient_section = cls(
            id=id,
            ingredients=ingredients,
            title=title,
        )

        return ingredient_section

