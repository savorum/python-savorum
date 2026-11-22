from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.meal_dish_recipe_status import MealDishRecipeStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.meal_plain_item import MealPlainItem





T = TypeVar("T", bound="MealDish")



@_attrs_define
class MealDish:
    """ 
        Attributes:
            display_name (str): A recipe dish named exactly as its recipe takes the recipe's new title when the recipe is
                renamed.
            entry_id (str | Unset):
            id (str | Unset):
            leftover_of (str | Unset): Source dish ID for leftovers. Omit entry_id on this dish to avoid repeating the
                recipe requirement.
            notes (str | Unset):
            plain_items (list[MealPlainItem] | None | Unset): Only for a dish without entry_id.
            recipe_image_url (str | Unset):
            recipe_revision (int | Unset):
            recipe_status (MealDishRecipeStatus | Unset):
            scale (str | Unset): Positive rational string multiplying the recipe quantities, such as 1/2 for half a batch.
                This is not a serving count.
            shopping_choices (list[str] | None | Unset):
     """

    display_name: str
    entry_id: str | Unset = UNSET
    id: str | Unset = UNSET
    leftover_of: str | Unset = UNSET
    notes: str | Unset = UNSET
    plain_items: list[MealPlainItem] | None | Unset = UNSET
    recipe_image_url: str | Unset = UNSET
    recipe_revision: int | Unset = UNSET
    recipe_status: MealDishRecipeStatus | Unset = UNSET
    scale: str | Unset = UNSET
    shopping_choices: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.meal_plain_item import MealPlainItem # noqa: PLC0415
        display_name = self.display_name

        entry_id = self.entry_id

        id = self.id

        leftover_of = self.leftover_of

        notes = self.notes

        plain_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.plain_items, Unset):
            plain_items = UNSET
        elif isinstance(self.plain_items, list):
            plain_items = []
            for plain_items_type_0_item_data in self.plain_items:
                plain_items_type_0_item = plain_items_type_0_item_data.to_dict()
                plain_items.append(plain_items_type_0_item)


        else:
            plain_items = self.plain_items

        recipe_image_url = self.recipe_image_url

        recipe_revision = self.recipe_revision

        recipe_status: str | Unset = UNSET
        if not isinstance(self.recipe_status, Unset):
            recipe_status = self.recipe_status.value


        scale = self.scale

        shopping_choices: list[str] | None | Unset
        if isinstance(self.shopping_choices, Unset):
            shopping_choices = UNSET
        elif isinstance(self.shopping_choices, list):
            shopping_choices = self.shopping_choices


        else:
            shopping_choices = self.shopping_choices


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "display_name": display_name,
        })
        if entry_id is not UNSET:
            field_dict["entry_id"] = entry_id
        if id is not UNSET:
            field_dict["id"] = id
        if leftover_of is not UNSET:
            field_dict["leftover_of"] = leftover_of
        if notes is not UNSET:
            field_dict["notes"] = notes
        if plain_items is not UNSET:
            field_dict["plain_items"] = plain_items
        if recipe_image_url is not UNSET:
            field_dict["recipe_image_url"] = recipe_image_url
        if recipe_revision is not UNSET:
            field_dict["recipe_revision"] = recipe_revision
        if recipe_status is not UNSET:
            field_dict["recipe_status"] = recipe_status
        if scale is not UNSET:
            field_dict["scale"] = scale
        if shopping_choices is not UNSET:
            field_dict["shopping_choices"] = shopping_choices

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meal_plain_item import MealPlainItem # noqa: PLC0415
        d = dict(src_dict)
        display_name = d.pop("display_name")

        entry_id = d.pop("entry_id", UNSET)

        id = d.pop("id", UNSET)

        leftover_of = d.pop("leftover_of", UNSET)

        notes = d.pop("notes", UNSET)

        def _parse_plain_items(data: object) -> list[MealPlainItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                plain_items_type_0 = []
                _plain_items_type_0 = data
                for plain_items_type_0_item_data in (_plain_items_type_0):
                    plain_items_type_0_item = MealPlainItem.from_dict(plain_items_type_0_item_data)



                    plain_items_type_0.append(plain_items_type_0_item)

                return plain_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MealPlainItem] | None | Unset, data)

        plain_items = _parse_plain_items(d.pop("plain_items", UNSET))


        recipe_image_url = d.pop("recipe_image_url", UNSET)

        recipe_revision = d.pop("recipe_revision", UNSET)

        _recipe_status = d.pop("recipe_status", UNSET)
        recipe_status: MealDishRecipeStatus | Unset
        if isinstance(_recipe_status,  Unset):
            recipe_status = UNSET
        else:
            recipe_status = MealDishRecipeStatus(_recipe_status)




        scale = d.pop("scale", UNSET)

        def _parse_shopping_choices(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                shopping_choices_type_0 = cast(list[str], data)

                return shopping_choices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        shopping_choices = _parse_shopping_choices(d.pop("shopping_choices", UNSET))


        meal_dish = cls(
            display_name=display_name,
            entry_id=entry_id,
            id=id,
            leftover_of=leftover_of,
            notes=notes,
            plain_items=plain_items,
            recipe_image_url=recipe_image_url,
            recipe_revision=recipe_revision,
            recipe_status=recipe_status,
            scale=scale,
            shopping_choices=shopping_choices,
        )

        return meal_dish

