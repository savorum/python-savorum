from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.account_user import AccountUser





T = TypeVar("T", bound="FinishNativeProviderLinkResponse200")



@_attrs_define
class FinishNativeProviderLinkResponse200:
    """ 
        Attributes:
            csrf_token (str):
            invitation_accepted (bool):
            user (AccountUser):
     """

    csrf_token: str
    invitation_accepted: bool
    user: AccountUser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_user import AccountUser # noqa: PLC0415
        csrf_token = self.csrf_token

        invitation_accepted = self.invitation_accepted

        user = self.user.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "csrf_token": csrf_token,
            "invitation_accepted": invitation_accepted,
            "user": user,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_user import AccountUser # noqa: PLC0415
        d = dict(src_dict)
        csrf_token = d.pop("csrf_token")

        invitation_accepted = d.pop("invitation_accepted")

        user = AccountUser.from_dict(d.pop("user"))




        finish_native_provider_link_response_200 = cls(
            csrf_token=csrf_token,
            invitation_accepted=invitation_accepted,
            user=user,
        )


        finish_native_provider_link_response_200.additional_properties = d
        return finish_native_provider_link_response_200

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
