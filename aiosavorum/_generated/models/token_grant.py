from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TokenGrant")



@_attrs_define
class TokenGrant:
    """ 
        Attributes:
            created_at (int):
            expires_at (int):
            id (str):
            last_used_at (int):
            libraries (list[str] | None):
            name (str):
            revoked_at (int):
            scopes (list[str] | None):
            secret (str):
     """

    created_at: int
    expires_at: int
    id: str
    last_used_at: int
    libraries: list[str] | None
    name: str
    revoked_at: int
    scopes: list[str] | None
    secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        expires_at = self.expires_at

        id = self.id

        last_used_at = self.last_used_at

        libraries: list[str] | None
        if isinstance(self.libraries, list):
            libraries = self.libraries


        else:
            libraries = self.libraries

        name = self.name

        revoked_at = self.revoked_at

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes


        else:
            scopes = self.scopes

        secret = self.secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "expires_at": expires_at,
            "id": id,
            "last_used_at": last_used_at,
            "libraries": libraries,
            "name": name,
            "revoked_at": revoked_at,
            "scopes": scopes,
            "secret": secret,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        expires_at = d.pop("expires_at")

        id = d.pop("id")

        last_used_at = d.pop("last_used_at")

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


        name = d.pop("name")

        revoked_at = d.pop("revoked_at")

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


        secret = d.pop("secret")

        token_grant = cls(
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            last_used_at=last_used_at,
            libraries=libraries,
            name=name,
            revoked_at=revoked_at,
            scopes=scopes,
            secret=secret,
        )


        token_grant.additional_properties = d
        return token_grant

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
