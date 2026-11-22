from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CapabilityToken")



@_attrs_define
class CapabilityToken:
    """ 
        Attributes:
            libraries (list[str] | None): Library IDs the token is limited to; empty means every library its owner can reach
            scopes (list[str] | None):
            expires_at (int | Unset): Unix time the token expires; absent when it does not expire
     """

    libraries: list[str] | None
    scopes: list[str] | None
    expires_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        libraries: list[str] | None
        if isinstance(self.libraries, list):
            libraries = self.libraries


        else:
            libraries = self.libraries

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes


        else:
            scopes = self.scopes

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "libraries": libraries,
            "scopes": scopes,
        })
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_libraries(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                libraries_type_0 = cast(list[str], data)

                return libraries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        libraries = _parse_libraries(d.pop("libraries"))


        def _parse_scopes(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        scopes = _parse_scopes(d.pop("scopes"))


        expires_at = d.pop("expires_at", UNSET)

        capability_token = cls(
            libraries=libraries,
            scopes=scopes,
            expires_at=expires_at,
        )


        capability_token.additional_properties = d
        return capability_token

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
