from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ImportPreviewAssets")



@_attrs_define
class ImportPreviewAssets:
    """ 
        Attributes:
            available (int):
            deferred (int):
            discovered (int):
            failed (int):
            unavailable (int):
            preview_url (str | Unset): Retrieves this recipe's leading photograph on demand; answers 404 with a problem type
                saying whether it is pending or unavailable
     """

    available: int
    deferred: int
    discovered: int
    failed: int
    unavailable: int
    preview_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        available = self.available

        deferred = self.deferred

        discovered = self.discovered

        failed = self.failed

        unavailable = self.unavailable

        preview_url = self.preview_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "available": available,
            "deferred": deferred,
            "discovered": discovered,
            "failed": failed,
            "unavailable": unavailable,
        })
        if preview_url is not UNSET:
            field_dict["preview_url"] = preview_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available")

        deferred = d.pop("deferred")

        discovered = d.pop("discovered")

        failed = d.pop("failed")

        unavailable = d.pop("unavailable")

        preview_url = d.pop("preview_url", UNSET)

        import_preview_assets = cls(
            available=available,
            deferred=deferred,
            discovered=discovered,
            failed=failed,
            unavailable=unavailable,
            preview_url=preview_url,
        )


        import_preview_assets.additional_properties = d
        return import_preview_assets

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
