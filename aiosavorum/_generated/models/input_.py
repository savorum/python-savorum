from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="Input")



@_attrs_define
class Input:
    """ 
        Attributes:
            enabled (bool):
            event_types (list[str] | None):
            name (str):
            url (str):
     """

    enabled: bool
    event_types: list[str] | None
    name: str
    url: str





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        event_types: list[str] | None
        if isinstance(self.event_types, list):
            event_types = self.event_types


        else:
            event_types = self.event_types

        name = self.name

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "enabled": enabled,
            "event_types": event_types,
            "name": name,
            "url": url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_event_types(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        event_types = _parse_event_types(d.pop("event_types"))


        name = d.pop("name")

        url = d.pop("url")

        input_ = cls(
            enabled=enabled,
            event_types=event_types,
            name=name,
            url=url,
        )

        return input_

