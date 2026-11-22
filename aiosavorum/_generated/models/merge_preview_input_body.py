from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MergePreviewInputBody")



@_attrs_define
class MergePreviewInputBody:
    """ 
        Attributes:
            left_id (str):
            right_id (str):
     """

    left_id: str
    right_id: str





    def to_dict(self) -> dict[str, Any]:
        left_id = self.left_id

        right_id = self.right_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "left_id": left_id,
            "right_id": right_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        left_id = d.pop("left_id")

        right_id = d.pop("right_id")

        merge_preview_input_body = cls(
            left_id=left_id,
            right_id=right_id,
        )

        return merge_preview_input_body

