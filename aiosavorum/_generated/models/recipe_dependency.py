from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RecipeDependency")



@_attrs_define
class RecipeDependency:
    """ 
        Attributes:
            entry_id (str | Unset): The active library entry carrying recipe_id, when one exists
            recipe_id (str | Unset): The other recipe's portable document ID, not a library entry ID
            title (str | Unset): The other recipe's title as authored
            url (str | Unset): Where the other recipe is published
     """

    entry_id: str | Unset = UNSET
    recipe_id: str | Unset = UNSET
    title: str | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        entry_id = self.entry_id

        recipe_id = self.recipe_id

        title = self.title

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entry_id is not UNSET:
            field_dict["entry_id"] = entry_id
        if recipe_id is not UNSET:
            field_dict["recipe_id"] = recipe_id
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry_id = d.pop("entry_id", UNSET)

        recipe_id = d.pop("recipe_id", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        recipe_dependency = cls(
            entry_id=entry_id,
            recipe_id=recipe_id,
            title=title,
            url=url,
        )

        return recipe_dependency

