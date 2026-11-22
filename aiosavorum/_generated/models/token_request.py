from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TokenRequest")



@_attrs_define
class TokenRequest:
    """ 
        Attributes:
            days (int):
            libraries (list[str] | None):
            name (str):
            nonexpiring (bool):
            scopes (list[str] | None):
     """

    days: int
    libraries: list[str] | None
    name: str
    nonexpiring: bool
    scopes: list[str] | None





    def to_dict(self) -> dict[str, Any]:
        days = self.days

        libraries: list[str] | None
        if isinstance(self.libraries, list):
            libraries = self.libraries


        else:
            libraries = self.libraries

        name = self.name

        nonexpiring = self.nonexpiring

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes


        else:
            scopes = self.scopes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "days": days,
            "libraries": libraries,
            "name": name,
            "nonexpiring": nonexpiring,
            "scopes": scopes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = d.pop("days")

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

        nonexpiring = d.pop("nonexpiring")

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


        token_request = cls(
            days=days,
            libraries=libraries,
            name=name,
            nonexpiring=nonexpiring,
            scopes=scopes,
        )

        return token_request

