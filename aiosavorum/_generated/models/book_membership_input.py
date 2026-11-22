from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BookMembershipInput")



@_attrs_define
class BookMembershipInput:
    """ 
        Attributes:
            book_id (str):
            member (bool): True to place the recipe in the book, false to take it out
            revision (int): Book revision this change expects
     """

    book_id: str
    member: bool
    revision: int





    def to_dict(self) -> dict[str, Any]:
        book_id = self.book_id

        member = self.member

        revision = self.revision


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "book_id": book_id,
            "member": member,
            "revision": revision,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        book_id = d.pop("book_id")

        member = d.pop("member")

        revision = d.pop("revision")

        book_membership_input = cls(
            book_id=book_id,
            member=member,
            revision=revision,
        )

        return book_membership_input

