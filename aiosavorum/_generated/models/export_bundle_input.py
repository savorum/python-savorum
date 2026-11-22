from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ExportBundleInput")



@_attrs_define
class ExportBundleInput:
    """ 
        Attributes:
            recipes (list[str] | None): Library entries to export, in the order they should appear in the bundle
     """

    recipes: list[str] | None





    def to_dict(self) -> dict[str, Any]:
        recipes: list[str] | None
        if isinstance(self.recipes, list):
            recipes = self.recipes


        else:
            recipes = self.recipes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "recipes": recipes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_recipes(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recipes_type_0 = cast(list[str], data)

                return recipes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        recipes = _parse_recipes(d.pop("recipes"))


        export_bundle_input = cls(
            recipes=recipes,
        )

        return export_bundle_input

