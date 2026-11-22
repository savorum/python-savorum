from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SavedMealSummary")



@_attrs_define
class SavedMealSummary:
    """ 
        Attributes:
            dish_count (int):
            dish_names (list[str] | None):
            id (str):
            name (str):
            revision (int):
     """

    dish_count: int
    dish_names: list[str] | None
    id: str
    name: str
    revision: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dish_count = self.dish_count

        dish_names: list[str] | None
        if isinstance(self.dish_names, list):
            dish_names = self.dish_names


        else:
            dish_names = self.dish_names

        id = self.id

        name = self.name

        revision = self.revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "dish_count": dish_count,
            "dish_names": dish_names,
            "id": id,
            "name": name,
            "revision": revision,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dish_count = d.pop("dish_count")

        def _parse_dish_names(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dish_names_type_0 = cast(list[str], data)

                return dish_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        dish_names = _parse_dish_names(d.pop("dish_names"))


        id = d.pop("id")

        name = d.pop("name")

        revision = d.pop("revision")

        saved_meal_summary = cls(
            dish_count=dish_count,
            dish_names=dish_names,
            id=id,
            name=name,
            revision=revision,
        )


        saved_meal_summary.additional_properties = d
        return saved_meal_summary

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
