from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.invitation import Invitation





T = TypeVar("T", bound="InvitationCreateResponse")



@_attrs_define
class InvitationCreateResponse:
    """ 
        Attributes:
            invitation (Invitation):
            token (str):
            url (str | Unset): Link to share, built from the configured public URL. Absent when none is configured.
     """

    invitation: Invitation
    token: str
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.invitation import Invitation # noqa: PLC0415
        invitation = self.invitation.to_dict()

        token = self.token

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "invitation": invitation,
            "token": token,
        })
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invitation import Invitation # noqa: PLC0415
        d = dict(src_dict)
        invitation = Invitation.from_dict(d.pop("invitation"))




        token = d.pop("token")

        url = d.pop("url", UNSET)

        invitation_create_response = cls(
            invitation=invitation,
            token=token,
            url=url,
        )


        invitation_create_response.additional_properties = d
        return invitation_create_response

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
