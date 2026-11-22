from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_input_on_duplicate import ImportInputOnDuplicate
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ImportInput")



@_attrs_define
class ImportInput:
    """ 
        Attributes:
            recipes (list[Any] | None): SREF recipe documents, each carrying its own sref version member
            on_duplicate (ImportInputOnDuplicate | Unset): Defaults to reject, which changes nothing and reports what was
                already here
     """

    recipes: list[Any] | None
    on_duplicate: ImportInputOnDuplicate | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        recipes: list[Any] | None
        if isinstance(self.recipes, list):
            recipes = self.recipes


        else:
            recipes = self.recipes

        on_duplicate: str | Unset = UNSET
        if not isinstance(self.on_duplicate, Unset):
            on_duplicate = self.on_duplicate.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "recipes": recipes,
        })
        if on_duplicate is not UNSET:
            field_dict["on_duplicate"] = on_duplicate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_recipes(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recipes_type_0 = cast(list[Any], data)

                return recipes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        recipes = _parse_recipes(d.pop("recipes"))


        _on_duplicate = d.pop("on_duplicate", UNSET)
        on_duplicate: ImportInputOnDuplicate | Unset
        if isinstance(_on_duplicate,  Unset):
            on_duplicate = UNSET
        else:
            on_duplicate = ImportInputOnDuplicate(_on_duplicate)




        import_input = cls(
            recipes=recipes,
            on_duplicate=on_duplicate,
        )

        return import_input

