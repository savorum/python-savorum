from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AssetReference")



@_attrs_define
class AssetReference:
    """ 
        Attributes:
            asset_id (str):
            local_asset_id (str):
            media_type (str):
            alt (str | Unset):
            caption (str | Unset):
            url (str | Unset): Immutable asset URL
     """

    asset_id: str
    local_asset_id: str
    media_type: str
    alt: str | Unset = UNSET
    caption: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        local_asset_id = self.local_asset_id

        media_type = self.media_type

        alt = self.alt

        caption = self.caption

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "asset_id": asset_id,
            "local_asset_id": local_asset_id,
            "media_type": media_type,
        })
        if alt is not UNSET:
            field_dict["alt"] = alt
        if caption is not UNSET:
            field_dict["caption"] = caption
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        local_asset_id = d.pop("local_asset_id")

        media_type = d.pop("media_type")

        alt = d.pop("alt", UNSET)

        caption = d.pop("caption", UNSET)

        url = d.pop("url", UNSET)

        asset_reference = cls(
            asset_id=asset_id,
            local_asset_id=local_asset_id,
            media_type=media_type,
            alt=alt,
            caption=caption,
            url=url,
        )


        asset_reference.additional_properties = d
        return asset_reference

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
