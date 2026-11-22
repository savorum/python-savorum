from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.invitation import Invitation





T = TypeVar("T", bound="InvitationListResponse")



@_attrs_define
class InvitationListResponse:
    """ 
        Attributes:
            invitations (list[Invitation] | None):
     """

    invitations: list[Invitation] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.invitation import Invitation # noqa: PLC0415
        invitations: list[dict[str, Any]] | None
        if isinstance(self.invitations, list):
            invitations = []
            for invitations_type_0_item_data in self.invitations:
                invitations_type_0_item = invitations_type_0_item_data.to_dict()
                invitations.append(invitations_type_0_item)


        else:
            invitations = self.invitations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "invitations": invitations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invitation import Invitation # noqa: PLC0415
        d = dict(src_dict)
        def _parse_invitations(data: object) -> list[Invitation] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                invitations_type_0 = []
                _invitations_type_0 = data
                for invitations_type_0_item_data in (_invitations_type_0):
                    invitations_type_0_item = Invitation.from_dict(invitations_type_0_item_data)



                    invitations_type_0.append(invitations_type_0_item)

                return invitations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Invitation] | None, data)

        invitations = _parse_invitations(d.pop("invitations"))


        invitation_list_response = cls(
            invitations=invitations,
        )


        invitation_list_response.additional_properties = d
        return invitation_list_response

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
