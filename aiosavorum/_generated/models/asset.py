from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.asset_role import AssetRole
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.asset_license import AssetLicense





T = TypeVar("T", bound="Asset")



@_attrs_define
class Asset:
    """ 
        Attributes:
            id (str):
            media_type (str):
            path (str):
            sha256 (str):
            size (int):
            alt (str | Unset):
            caption (str | Unset):
            creator (str | Unset): Who the source credits with creating the file
            credit (str | Unset): Authored credit line
            license_ (AssetLicense | Unset):
            rights (str | Unset): Authored copyright or rights statement
            role (AssetRole | Unset):
            source_url (str | Unset): Page or file the asset came from
     """

    id: str
    media_type: str
    path: str
    sha256: str
    size: int
    alt: str | Unset = UNSET
    caption: str | Unset = UNSET
    creator: str | Unset = UNSET
    credit: str | Unset = UNSET
    license_: AssetLicense | Unset = UNSET
    rights: str | Unset = UNSET
    role: AssetRole | Unset = UNSET
    source_url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_license import AssetLicense # noqa: PLC0415
        id = self.id

        media_type = self.media_type

        path = self.path

        sha256 = self.sha256

        size = self.size

        alt = self.alt

        caption = self.caption

        creator = self.creator

        credit = self.credit

        license_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        rights = self.rights

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value


        source_url = self.source_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "media_type": media_type,
            "path": path,
            "sha256": sha256,
            "size": size,
        })
        if alt is not UNSET:
            field_dict["alt"] = alt
        if caption is not UNSET:
            field_dict["caption"] = caption
        if creator is not UNSET:
            field_dict["creator"] = creator
        if credit is not UNSET:
            field_dict["credit"] = credit
        if license_ is not UNSET:
            field_dict["license"] = license_
        if rights is not UNSET:
            field_dict["rights"] = rights
        if role is not UNSET:
            field_dict["role"] = role
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_license import AssetLicense # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        media_type = d.pop("media_type")

        path = d.pop("path")

        sha256 = d.pop("sha256")

        size = d.pop("size")

        alt = d.pop("alt", UNSET)

        caption = d.pop("caption", UNSET)

        creator = d.pop("creator", UNSET)

        credit = d.pop("credit", UNSET)

        _license_ = d.pop("license", UNSET)
        license_: AssetLicense | Unset
        if isinstance(_license_,  Unset):
            license_ = UNSET
        else:
            license_ = AssetLicense.from_dict(_license_)




        rights = d.pop("rights", UNSET)

        _role = d.pop("role", UNSET)
        role: AssetRole | Unset
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = AssetRole(_role)




        source_url = d.pop("source_url", UNSET)

        asset = cls(
            id=id,
            media_type=media_type,
            path=path,
            sha256=sha256,
            size=size,
            alt=alt,
            caption=caption,
            creator=creator,
            credit=credit,
            license_=license_,
            rights=rights,
            role=role,
            source_url=source_url,
        )

        return asset

