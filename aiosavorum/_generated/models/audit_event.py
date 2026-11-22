from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AuditEvent")



@_attrs_define
class AuditEvent:
    """ 
        Attributes:
            action (str):
            actor_id (str):
            correlation_id (str):
            created_at (int):
            credential_id (str):
            id (int):
            library_id (str):
            outcome (str):
            target_id (str):
            target_type (str):
     """

    action: str
    actor_id: str
    correlation_id: str
    created_at: int
    credential_id: str
    id: int
    library_id: str
    outcome: str
    target_id: str
    target_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action

        actor_id = self.actor_id

        correlation_id = self.correlation_id

        created_at = self.created_at

        credential_id = self.credential_id

        id = self.id

        library_id = self.library_id

        outcome = self.outcome

        target_id = self.target_id

        target_type = self.target_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
            "actor_id": actor_id,
            "correlation_id": correlation_id,
            "created_at": created_at,
            "credential_id": credential_id,
            "id": id,
            "library_id": library_id,
            "outcome": outcome,
            "target_id": target_id,
            "target_type": target_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        actor_id = d.pop("actor_id")

        correlation_id = d.pop("correlation_id")

        created_at = d.pop("created_at")

        credential_id = d.pop("credential_id")

        id = d.pop("id")

        library_id = d.pop("library_id")

        outcome = d.pop("outcome")

        target_id = d.pop("target_id")

        target_type = d.pop("target_type")

        audit_event = cls(
            action=action,
            actor_id=actor_id,
            correlation_id=correlation_id,
            created_at=created_at,
            credential_id=credential_id,
            id=id,
            library_id=library_id,
            outcome=outcome,
            target_id=target_id,
            target_type=target_type,
        )


        audit_event.additional_properties = d
        return audit_event

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
