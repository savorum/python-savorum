from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SelectLibraryRequest")



@_attrs_define
class SelectLibraryRequest:
    """ 
        Attributes:
            library_id (str):
     """

    library_id: str





    def to_dict(self) -> dict[str, Any]:
        library_id = self.library_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "library_id": library_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        library_id = d.pop("library_id")

        select_library_request = cls(
            library_id=library_id,
        )

        return select_library_request

