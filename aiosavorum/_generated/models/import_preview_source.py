from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ImportPreviewSource")



@_attrs_define
class ImportPreviewSource:
    """ 
        Attributes:
            can_retain (bool): The uploaded original can be retained explicitly when this preview item is committed
            format_id (str):
            format_name (str):
            attribution (str | Unset):
            extracted_text (str | Unset): Text extracted from a document upload, editable before commit
            filename (str | Unset):
            shared_from (str | Unset): The social post that led to url
            url (str | Unset):
     """

    can_retain: bool
    format_id: str
    format_name: str
    attribution: str | Unset = UNSET
    extracted_text: str | Unset = UNSET
    filename: str | Unset = UNSET
    shared_from: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        can_retain = self.can_retain

        format_id = self.format_id

        format_name = self.format_name

        attribution = self.attribution

        extracted_text = self.extracted_text

        filename = self.filename

        shared_from = self.shared_from

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "can_retain": can_retain,
            "format_id": format_id,
            "format_name": format_name,
        })
        if attribution is not UNSET:
            field_dict["attribution"] = attribution
        if extracted_text is not UNSET:
            field_dict["extracted_text"] = extracted_text
        if filename is not UNSET:
            field_dict["filename"] = filename
        if shared_from is not UNSET:
            field_dict["shared_from"] = shared_from
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_retain = d.pop("can_retain")

        format_id = d.pop("format_id")

        format_name = d.pop("format_name")

        attribution = d.pop("attribution", UNSET)

        extracted_text = d.pop("extracted_text", UNSET)

        filename = d.pop("filename", UNSET)

        shared_from = d.pop("shared_from", UNSET)

        url = d.pop("url", UNSET)

        import_preview_source = cls(
            can_retain=can_retain,
            format_id=format_id,
            format_name=format_name,
            attribution=attribution,
            extracted_text=extracted_text,
            filename=filename,
            shared_from=shared_from,
            url=url,
        )


        import_preview_source.additional_properties = d
        return import_preview_source

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
