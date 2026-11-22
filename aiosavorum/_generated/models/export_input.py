from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.export_input_format import ExportInputFormat
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ExportInput")



@_attrs_define
class ExportInput:
    """ 
        Attributes:
            format_ (ExportInputFormat):
            library (bool | Unset):
            recipes (list[str] | None | Unset):
     """

    format_: ExportInputFormat
    library: bool | Unset = UNSET
    recipes: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        library = self.library

        recipes: list[str] | None | Unset
        if isinstance(self.recipes, Unset):
            recipes = UNSET
        elif isinstance(self.recipes, list):
            recipes = self.recipes


        else:
            recipes = self.recipes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "format": format_,
        })
        if library is not UNSET:
            field_dict["library"] = library
        if recipes is not UNSET:
            field_dict["recipes"] = recipes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = ExportInputFormat(d.pop("format"))




        library = d.pop("library", UNSET)

        def _parse_recipes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recipes_type_0 = cast(list[str], data)

                return recipes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        recipes = _parse_recipes(d.pop("recipes", UNSET))


        export_input = cls(
            format_=format_,
            library=library,
            recipes=recipes,
        )

        return export_input

