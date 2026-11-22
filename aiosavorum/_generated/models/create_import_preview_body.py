from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from io import BytesIO






T = TypeVar("T", bound="CreateImportPreviewBody")



@_attrs_define
class CreateImportPreviewBody:
    

    additional_properties: dict[str, File] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_tuple()



        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []


        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, prop.to_tuple()))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_import_preview_body = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = File(
                 payload = BytesIO(prop_dict)
            )



            additional_properties[prop_name] = additional_property

        create_import_preview_body.additional_properties = additional_properties
        return create_import_preview_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> File:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: File) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
