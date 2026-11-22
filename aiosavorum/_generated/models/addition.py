from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Addition")



@_attrs_define
class Addition:
    """ 
        Attributes:
            id (str):
            name (str):
            buy (str | Unset):
            category (str | Unset):
            note (str | Unset):
     """

    id: str
    name: str
    buy: str | Unset = UNSET
    category: str | Unset = UNSET
    note: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        buy = self.buy

        category = self.category

        note = self.note


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
        })
        if buy is not UNSET:
            field_dict["buy"] = buy
        if category is not UNSET:
            field_dict["category"] = category
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        buy = d.pop("buy", UNSET)

        category = d.pop("category", UNSET)

        note = d.pop("note", UNSET)

        addition = cls(
            id=id,
            name=name,
            buy=buy,
            category=category,
            note=note,
        )

        return addition

