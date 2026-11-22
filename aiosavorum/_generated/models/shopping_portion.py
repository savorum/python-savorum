from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ShoppingPortion")



@_attrs_define
class ShoppingPortion:
    """ 
        Attributes:
            id (str):
            recipe_id (str):
            revision (int | Unset):
            scale (str | Unset):
     """

    id: str
    recipe_id: str
    revision: int | Unset = UNSET
    scale: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        recipe_id = self.recipe_id

        revision = self.revision

        scale = self.scale


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "recipe_id": recipe_id,
        })
        if revision is not UNSET:
            field_dict["revision"] = revision
        if scale is not UNSET:
            field_dict["scale"] = scale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        recipe_id = d.pop("recipe_id")

        revision = d.pop("revision", UNSET)

        scale = d.pop("scale", UNSET)

        shopping_portion = cls(
            id=id,
            recipe_id=recipe_id,
            revision=revision,
            scale=scale,
        )

        return shopping_portion

