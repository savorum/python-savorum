from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Subscription")



@_attrs_define
class Subscription:
    """ 
        Attributes:
            consecutive_failures (int):
            created_at (datetime.datetime):
            enabled (bool):
            event_types (list[str] | None):
            id (str):
            name (str):
            revision (int):
            secret_rotated_at (datetime.datetime):
            updated_at (datetime.datetime):
            updated_by (str):
            url (str):
            library_id (str | Unset):
            pause_reason (str | Unset):
     """

    consecutive_failures: int
    created_at: datetime.datetime
    enabled: bool
    event_types: list[str] | None
    id: str
    name: str
    revision: int
    secret_rotated_at: datetime.datetime
    updated_at: datetime.datetime
    updated_by: str
    url: str
    library_id: str | Unset = UNSET
    pause_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        consecutive_failures = self.consecutive_failures

        created_at = self.created_at.isoformat()

        enabled = self.enabled

        event_types: list[str] | None
        if isinstance(self.event_types, list):
            event_types = self.event_types


        else:
            event_types = self.event_types

        id = self.id

        name = self.name

        revision = self.revision

        secret_rotated_at = self.secret_rotated_at.isoformat()

        updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by

        url = self.url

        library_id = self.library_id

        pause_reason = self.pause_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "consecutive_failures": consecutive_failures,
            "created_at": created_at,
            "enabled": enabled,
            "event_types": event_types,
            "id": id,
            "name": name,
            "revision": revision,
            "secret_rotated_at": secret_rotated_at,
            "updated_at": updated_at,
            "updated_by": updated_by,
            "url": url,
        })
        if library_id is not UNSET:
            field_dict["library_id"] = library_id
        if pause_reason is not UNSET:
            field_dict["pause_reason"] = pause_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consecutive_failures = d.pop("consecutive_failures")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        enabled = d.pop("enabled")

        def _parse_event_types(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        event_types = _parse_event_types(d.pop("event_types"))


        id = d.pop("id")

        name = d.pop("name")

        revision = d.pop("revision")

        secret_rotated_at = datetime.datetime.fromisoformat(d.pop("secret_rotated_at"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        updated_by = d.pop("updated_by")

        url = d.pop("url")

        library_id = d.pop("library_id", UNSET)

        pause_reason = d.pop("pause_reason", UNSET)

        subscription = cls(
            consecutive_failures=consecutive_failures,
            created_at=created_at,
            enabled=enabled,
            event_types=event_types,
            id=id,
            name=name,
            revision=revision,
            secret_rotated_at=secret_rotated_at,
            updated_at=updated_at,
            updated_by=updated_by,
            url=url,
            library_id=library_id,
            pause_reason=pause_reason,
        )


        subscription.additional_properties = d
        return subscription

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
