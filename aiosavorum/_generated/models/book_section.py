from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BookSection")



@_attrs_define
class BookSection:
    """ 
        Attributes:
            position (int):
            title (str):
            id (str | Unset):
     """

    position: int
    title: str
    id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        position = self.position

        title = self.title

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "position": position,
            "title": title,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position")

        title = d.pop("title")

        id = d.pop("id", UNSET)

        book_section = cls(
            position=position,
            title=title,
            id=id,
        )

        return book_section

