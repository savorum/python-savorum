from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Delivery")



@_attrs_define
class Delivery:
    """ 
        Attributes:
            attempts (int):
            created_at (datetime.datetime):
            event_id (str):
            event_type (str):
            id (str):
            state (str):
            subscription_id (str):
            last_code (str | Unset):
            next_attempt_at (datetime.datetime | Unset):
     """

    attempts: int
    created_at: datetime.datetime
    event_id: str
    event_type: str
    id: str
    state: str
    subscription_id: str
    last_code: str | Unset = UNSET
    next_attempt_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        created_at = self.created_at.isoformat()

        event_id = self.event_id

        event_type = self.event_type

        id = self.id

        state = self.state

        subscription_id = self.subscription_id

        last_code = self.last_code

        next_attempt_at: str | Unset = UNSET
        if not isinstance(self.next_attempt_at, Unset):
            next_attempt_at = self.next_attempt_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "attempts": attempts,
            "created_at": created_at,
            "event_id": event_id,
            "event_type": event_type,
            "id": id,
            "state": state,
            "subscription_id": subscription_id,
        })
        if last_code is not UNSET:
            field_dict["last_code"] = last_code
        if next_attempt_at is not UNSET:
            field_dict["next_attempt_at"] = next_attempt_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        event_id = d.pop("event_id")

        event_type = d.pop("event_type")

        id = d.pop("id")

        state = d.pop("state")

        subscription_id = d.pop("subscription_id")

        last_code = d.pop("last_code", UNSET)

        _next_attempt_at = d.pop("next_attempt_at", UNSET)
        next_attempt_at: datetime.datetime | Unset
        if isinstance(_next_attempt_at,  Unset):
            next_attempt_at = UNSET
        else:
            next_attempt_at = datetime.datetime.fromisoformat(_next_attempt_at)




        delivery = cls(
            attempts=attempts,
            created_at=created_at,
            event_id=event_id,
            event_type=event_type,
            id=id,
            state=state,
            subscription_id=subscription_id,
            last_code=last_code,
            next_attempt_at=next_attempt_at,
        )


        delivery.additional_properties = d
        return delivery

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
