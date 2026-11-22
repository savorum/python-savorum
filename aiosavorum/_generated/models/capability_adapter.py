from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CapabilityAdapter")



@_attrs_define
class CapabilityAdapter:
    """ 
        Attributes:
            collection (bool):
            id (str):
            name (str):
            extensions (list[str] | None | Unset):
            input_kinds (list[str] | None | Unset):
            media_types (list[str] | None | Unset):
            version (str | Unset):
     """

    collection: bool
    id: str
    name: str
    extensions: list[str] | None | Unset = UNSET
    input_kinds: list[str] | None | Unset = UNSET
    media_types: list[str] | None | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        collection = self.collection

        id = self.id

        name = self.name

        extensions: list[str] | None | Unset
        if isinstance(self.extensions, Unset):
            extensions = UNSET
        elif isinstance(self.extensions, list):
            extensions = self.extensions


        else:
            extensions = self.extensions

        input_kinds: list[str] | None | Unset
        if isinstance(self.input_kinds, Unset):
            input_kinds = UNSET
        elif isinstance(self.input_kinds, list):
            input_kinds = self.input_kinds


        else:
            input_kinds = self.input_kinds

        media_types: list[str] | None | Unset
        if isinstance(self.media_types, Unset):
            media_types = UNSET
        elif isinstance(self.media_types, list):
            media_types = self.media_types


        else:
            media_types = self.media_types

        version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "collection": collection,
            "id": id,
            "name": name,
        })
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if input_kinds is not UNSET:
            field_dict["input_kinds"] = input_kinds
        if media_types is not UNSET:
            field_dict["media_types"] = media_types
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection = d.pop("collection")

        id = d.pop("id")

        name = d.pop("name")

        def _parse_extensions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extensions_type_0 = cast(list[str], data)

                return extensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extensions = _parse_extensions(d.pop("extensions", UNSET))


        def _parse_input_kinds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_kinds_type_0 = cast(list[str], data)

                return input_kinds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        input_kinds = _parse_input_kinds(d.pop("input_kinds", UNSET))


        def _parse_media_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_types_type_0 = cast(list[str], data)

                return media_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        media_types = _parse_media_types(d.pop("media_types", UNSET))


        version = d.pop("version", UNSET)

        capability_adapter = cls(
            collection=collection,
            id=id,
            name=name,
            extensions=extensions,
            input_kinds=input_kinds,
            media_types=media_types,
            version=version,
        )


        capability_adapter.additional_properties = d
        return capability_adapter

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
