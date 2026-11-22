from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SourceAttachmentResource")



@_attrs_define
class SourceAttachmentResource:
    """ 
        Attributes:
            asset_id (str):
            filename (str):
            media_type (str):
            revision (int):
            size (int):
            url (str):
     """

    asset_id: str
    filename: str
    media_type: str
    revision: int
    size: int
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        filename = self.filename

        media_type = self.media_type

        revision = self.revision

        size = self.size

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "asset_id": asset_id,
            "filename": filename,
            "media_type": media_type,
            "revision": revision,
            "size": size,
            "url": url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        filename = d.pop("filename")

        media_type = d.pop("media_type")

        revision = d.pop("revision")

        size = d.pop("size")

        url = d.pop("url")

        source_attachment_resource = cls(
            asset_id=asset_id,
            filename=filename,
            media_type=media_type,
            revision=revision,
            size=size,
            url=url,
        )


        source_attachment_resource.additional_properties = d
        return source_attachment_resource

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
