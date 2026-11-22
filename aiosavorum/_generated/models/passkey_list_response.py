from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.passkey import Passkey





T = TypeVar("T", bound="PasskeyListResponse")



@_attrs_define
class PasskeyListResponse:
    """ 
        Attributes:
            available (bool): Whether the current origin can register or use a passkey
            passkeys (list[Passkey] | None):
     """

    available: bool
    passkeys: list[Passkey] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.passkey import Passkey # noqa: PLC0415
        available = self.available

        passkeys: list[dict[str, Any]] | None
        if isinstance(self.passkeys, list):
            passkeys = []
            for passkeys_type_0_item_data in self.passkeys:
                passkeys_type_0_item = passkeys_type_0_item_data.to_dict()
                passkeys.append(passkeys_type_0_item)


        else:
            passkeys = self.passkeys


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "available": available,
            "passkeys": passkeys,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.passkey import Passkey # noqa: PLC0415
        d = dict(src_dict)
        available = d.pop("available")

        def _parse_passkeys(data: object) -> list[Passkey] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                passkeys_type_0 = []
                _passkeys_type_0 = data
                for passkeys_type_0_item_data in (_passkeys_type_0):
                    passkeys_type_0_item = Passkey.from_dict(passkeys_type_0_item_data)



                    passkeys_type_0.append(passkeys_type_0_item)

                return passkeys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Passkey] | None, data)

        passkeys = _parse_passkeys(d.pop("passkeys"))


        passkey_list_response = cls(
            available=available,
            passkeys=passkeys,
        )


        passkey_list_response.additional_properties = d
        return passkey_list_response

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
