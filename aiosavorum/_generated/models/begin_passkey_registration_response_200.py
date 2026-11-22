from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.begin_passkey_registration_response_200_public_key import BeginPasskeyRegistrationResponse200PublicKey





T = TypeVar("T", bound="BeginPasskeyRegistrationResponse200")



@_attrs_define
class BeginPasskeyRegistrationResponse200:
    """ 
        Attributes:
            public_key (BeginPasskeyRegistrationResponse200PublicKey): WebAuthn PublicKeyCredentialCreationOptions or
                PublicKeyCredentialRequestOptions, as the browser API takes them.
     """

    public_key: BeginPasskeyRegistrationResponse200PublicKey
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.begin_passkey_registration_response_200_public_key import BeginPasskeyRegistrationResponse200PublicKey # noqa: PLC0415
        public_key = self.public_key.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "publicKey": public_key,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.begin_passkey_registration_response_200_public_key import BeginPasskeyRegistrationResponse200PublicKey # noqa: PLC0415
        d = dict(src_dict)
        public_key = BeginPasskeyRegistrationResponse200PublicKey.from_dict(d.pop("publicKey"))




        begin_passkey_registration_response_200 = cls(
            public_key=public_key,
        )


        begin_passkey_registration_response_200.additional_properties = d
        return begin_passkey_registration_response_200

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
