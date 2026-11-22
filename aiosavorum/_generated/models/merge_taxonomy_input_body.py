from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MergeTaxonomyInputBody")



@_attrs_define
class MergeTaxonomyInputBody:
    """ 
        Attributes:
            target_id (str):
     """

    target_id: str





    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "target_id": target_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_id = d.pop("target_id")

        merge_taxonomy_input_body = cls(
            target_id=target_id,
        )

        return merge_taxonomy_input_body

