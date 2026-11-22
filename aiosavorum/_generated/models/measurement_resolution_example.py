from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MeasurementResolutionExample")



@_attrs_define
class MeasurementResolutionExample:
    """ 
        Attributes:
            before (str):
            recipe_title (str):
            source_text (str):
            after (str | Unset):
     """

    before: str
    recipe_title: str
    source_text: str
    after: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        before = self.before

        recipe_title = self.recipe_title

        source_text = self.source_text

        after = self.after


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "before": before,
            "recipe_title": recipe_title,
            "source_text": source_text,
        })
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        before = d.pop("before")

        recipe_title = d.pop("recipe_title")

        source_text = d.pop("source_text")

        after = d.pop("after", UNSET)

        measurement_resolution_example = cls(
            before=before,
            recipe_title=recipe_title,
            source_text=source_text,
            after=after,
        )


        measurement_resolution_example.additional_properties = d
        return measurement_resolution_example

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
