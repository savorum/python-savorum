from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CompleteSamlLoginBody")



@_attrs_define
class CompleteSamlLoginBody:
    """ 
        Attributes:
            relay_state (str):
            saml_response (str):
     """

    relay_state: str
    saml_response: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        relay_state = self.relay_state

        saml_response = self.saml_response


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "RelayState": relay_state,
            "SAMLResponse": saml_response,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        relay_state = d.pop("RelayState")

        saml_response = d.pop("SAMLResponse")

        complete_saml_login_body = cls(
            relay_state=relay_state,
            saml_response=saml_response,
        )


        complete_saml_login_body.additional_properties = d
        return complete_saml_login_body

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
