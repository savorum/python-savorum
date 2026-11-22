from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_preview_section import ImportPreviewSection





T = TypeVar("T", bound="ImportPreviewRecipe")



@_attrs_define
class ImportPreviewRecipe:
    """ 
        Attributes:
            ingredient_count (int):
            step_count (int):
            title (str):
            description (str | Unset):
            ingredients (list[ImportPreviewSection] | None | Unset):
            instructions (list[ImportPreviewSection] | None | Unset):
            yield_ (str | Unset):
     """

    ingredient_count: int
    step_count: int
    title: str
    description: str | Unset = UNSET
    ingredients: list[ImportPreviewSection] | None | Unset = UNSET
    instructions: list[ImportPreviewSection] | None | Unset = UNSET
    yield_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_preview_section import ImportPreviewSection # noqa: PLC0415
        ingredient_count = self.ingredient_count

        step_count = self.step_count

        title = self.title

        description = self.description

        ingredients: list[dict[str, Any]] | None | Unset
        if isinstance(self.ingredients, Unset):
            ingredients = UNSET
        elif isinstance(self.ingredients, list):
            ingredients = []
            for ingredients_type_0_item_data in self.ingredients:
                ingredients_type_0_item = ingredients_type_0_item_data.to_dict()
                ingredients.append(ingredients_type_0_item)


        else:
            ingredients = self.ingredients

        instructions: list[dict[str, Any]] | None | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        elif isinstance(self.instructions, list):
            instructions = []
            for instructions_type_0_item_data in self.instructions:
                instructions_type_0_item = instructions_type_0_item_data.to_dict()
                instructions.append(instructions_type_0_item)


        else:
            instructions = self.instructions

        yield_ = self.yield_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ingredient_count": ingredient_count,
            "step_count": step_count,
            "title": title,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if ingredients is not UNSET:
            field_dict["ingredients"] = ingredients
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if yield_ is not UNSET:
            field_dict["yield"] = yield_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_preview_section import ImportPreviewSection # noqa: PLC0415
        d = dict(src_dict)
        ingredient_count = d.pop("ingredient_count")

        step_count = d.pop("step_count")

        title = d.pop("title")

        description = d.pop("description", UNSET)

        def _parse_ingredients(data: object) -> list[ImportPreviewSection] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ingredients_type_0 = []
                _ingredients_type_0 = data
                for ingredients_type_0_item_data in (_ingredients_type_0):
                    ingredients_type_0_item = ImportPreviewSection.from_dict(ingredients_type_0_item_data)



                    ingredients_type_0.append(ingredients_type_0_item)

                return ingredients_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportPreviewSection] | None | Unset, data)

        ingredients = _parse_ingredients(d.pop("ingredients", UNSET))


        def _parse_instructions(data: object) -> list[ImportPreviewSection] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instructions_type_0 = []
                _instructions_type_0 = data
                for instructions_type_0_item_data in (_instructions_type_0):
                    instructions_type_0_item = ImportPreviewSection.from_dict(instructions_type_0_item_data)



                    instructions_type_0.append(instructions_type_0_item)

                return instructions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportPreviewSection] | None | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        yield_ = d.pop("yield", UNSET)

        import_preview_recipe = cls(
            ingredient_count=ingredient_count,
            step_count=step_count,
            title=title,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            yield_=yield_,
        )


        import_preview_recipe.additional_properties = d
        return import_preview_recipe

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
