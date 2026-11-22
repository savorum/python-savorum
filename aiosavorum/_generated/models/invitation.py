from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="Invitation")



@_attrs_define
class Invitation:
    """ 
        Attributes:
            accepted_at (int | None):
            created_at (int):
            creator (str):
            expires_at (int):
            hint (str):
            id (str):
            library_id (str):
            revoked_at (int | None):
            role (str):
     """

    accepted_at: int | None
    created_at: int
    creator: str
    expires_at: int
    hint: str
    id: str
    library_id: str
    revoked_at: int | None
    role: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        accepted_at: int | None
        accepted_at = self.accepted_at

        created_at = self.created_at

        creator = self.creator

        expires_at = self.expires_at

        hint = self.hint

        id = self.id

        library_id = self.library_id

        revoked_at: int | None
        revoked_at = self.revoked_at

        role = self.role


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accepted_at": accepted_at,
            "created_at": created_at,
            "creator": creator,
            "expires_at": expires_at,
            "hint": hint,
            "id": id,
            "library_id": library_id,
            "revoked_at": revoked_at,
            "role": role,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_accepted_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        accepted_at = _parse_accepted_at(d.pop("accepted_at"))


        created_at = d.pop("created_at")

        creator = d.pop("creator")

        expires_at = d.pop("expires_at")

        hint = d.pop("hint")

        id = d.pop("id")

        library_id = d.pop("library_id")

        def _parse_revoked_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))


        role = d.pop("role")

        invitation = cls(
            accepted_at=accepted_at,
            created_at=created_at,
            creator=creator,
            expires_at=expires_at,
            hint=hint,
            id=id,
            library_id=library_id,
            revoked_at=revoked_at,
            role=role,
        )


        invitation.additional_properties = d
        return invitation

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
