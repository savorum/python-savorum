from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="AssetBlob")



@_attrs_define
class AssetBlob:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (str):
            media_type (str):
            sha256 (str):
            size (int):
     """

    created_at: datetime.datetime
    id: str
    media_type: str
    sha256: str
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        media_type = self.media_type

        sha256 = self.sha256

        size = self.size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "media_type": media_type,
            "sha256": sha256,
            "size": size,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        media_type = d.pop("media_type")

        sha256 = d.pop("sha256")

        size = d.pop("size")

        asset_blob = cls(
            created_at=created_at,
            id=id,
            media_type=media_type,
            sha256=sha256,
            size=size,
        )


        asset_blob.additional_properties = d
        return asset_blob

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
