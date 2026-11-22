from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GroupMapping")



@_attrs_define
class GroupMapping:
    """ 
        Attributes:
            group (str):
            id (str):
            library_id (str):
            provider_id (str):
            role (str):
     """

    group: str
    id: str
    library_id: str
    provider_id: str
    role: str





    def to_dict(self) -> dict[str, Any]:
        group = self.group

        id = self.id

        library_id = self.library_id

        provider_id = self.provider_id

        role = self.role


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "group": group,
            "id": id,
            "library_id": library_id,
            "provider_id": provider_id,
            "role": role,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group = d.pop("group")

        id = d.pop("id")

        library_id = d.pop("library_id")

        provider_id = d.pop("provider_id")

        role = d.pop("role")

        group_mapping = cls(
            group=group,
            id=id,
            library_id=library_id,
            provider_id=provider_id,
            role=role,
        )

        return group_mapping

