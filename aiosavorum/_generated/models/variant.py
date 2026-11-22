from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Variant")



@_attrs_define
class Variant:
    """ 
        Attributes:
            text (str):
            id (str | Unset): Recipe-local identifier that claims use to scope themselves to this variant
            title (str | Unset):
     """

    text: str
    id: str | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        text = self.text

        id = self.id

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        variant = cls(
            text=text,
            id=id,
            title=title,
        )

        return variant

