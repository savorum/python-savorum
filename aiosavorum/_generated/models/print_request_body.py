from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.print_options import PrintOptions





T = TypeVar("T", bound="PrintRequestBody")



@_attrs_define
class PrintRequestBody:
    """ 
        Attributes:
            book (str | Unset): Book to print instead of a recipe selection
            options (PrintOptions | Unset):
            recipes (list[str] | None | Unset): Library entries to print, in the order they should appear. Capabilities
                report the most one document holds.
     """

    book: str | Unset = UNSET
    options: PrintOptions | Unset = UNSET
    recipes: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.print_options import PrintOptions # noqa: PLC0415
        book = self.book

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        recipes: list[str] | None | Unset
        if isinstance(self.recipes, Unset):
            recipes = UNSET
        elif isinstance(self.recipes, list):
            recipes = self.recipes


        else:
            recipes = self.recipes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if book is not UNSET:
            field_dict["book"] = book
        if options is not UNSET:
            field_dict["options"] = options
        if recipes is not UNSET:
            field_dict["recipes"] = recipes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.print_options import PrintOptions # noqa: PLC0415
        d = dict(src_dict)
        book = d.pop("book", UNSET)

        _options = d.pop("options", UNSET)
        options: PrintOptions | Unset
        if isinstance(_options,  Unset):
            options = UNSET
        else:
            options = PrintOptions.from_dict(_options)




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


        print_request_body = cls(
            book=book,
            options=options,
            recipes=recipes,
        )

        return print_request_body

