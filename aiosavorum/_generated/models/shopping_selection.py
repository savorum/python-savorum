from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ShoppingSelection")



@_attrs_define
class ShoppingSelection:
    """ 
        Attributes:
            choice_id (str):
            id (str):
            selected (bool):
     """

    choice_id: str
    id: str
    selected: bool





    def to_dict(self) -> dict[str, Any]:
        choice_id = self.choice_id

        id = self.id

        selected = self.selected


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "choice_id": choice_id,
            "id": id,
            "selected": selected,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        choice_id = d.pop("choice_id")

        id = d.pop("id")

        selected = d.pop("selected")

        shopping_selection = cls(
            choice_id=choice_id,
            id=id,
            selected=selected,
        )

        return shopping_selection

