from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CapabilityLinks")



@_attrs_define
class CapabilityLinks:
    """ 
        Attributes:
            guide (str): Guide for agents and integrations, written for this instance's version
            openapi (str): OpenAPI description of this API
            tokens (str): Page where a signed-in person creates personal API tokens
     """

    guide: str
    openapi: str
    tokens: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        guide = self.guide

        openapi = self.openapi

        tokens = self.tokens


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guide": guide,
            "openapi": openapi,
            "tokens": tokens,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guide = d.pop("guide")

        openapi = d.pop("openapi")

        tokens = d.pop("tokens")

        capability_links = cls(
            guide=guide,
            openapi=openapi,
            tokens=tokens,
        )


        capability_links.additional_properties = d
        return capability_links

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
