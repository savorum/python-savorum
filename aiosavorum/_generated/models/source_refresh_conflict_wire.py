from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SourceRefreshConflictWire")



@_attrs_define
class SourceRefreshConflictWire:
    """ 
        Attributes:
            area (str):
            path (str):
            base (str | Unset):
            local (str | Unset):
            remote (str | Unset):
     """

    area: str
    path: str
    base: str | Unset = UNSET
    local: str | Unset = UNSET
    remote: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        area = self.area

        path = self.path

        base = self.base

        local = self.local

        remote = self.remote


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "area": area,
            "path": path,
        })
        if base is not UNSET:
            field_dict["base"] = base
        if local is not UNSET:
            field_dict["local"] = local
        if remote is not UNSET:
            field_dict["remote"] = remote

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        area = d.pop("area")

        path = d.pop("path")

        base = d.pop("base", UNSET)

        local = d.pop("local", UNSET)

        remote = d.pop("remote", UNSET)

        source_refresh_conflict_wire = cls(
            area=area,
            path=path,
            base=base,
            local=local,
            remote=remote,
        )


        source_refresh_conflict_wire.additional_properties = d
        return source_refresh_conflict_wire

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
