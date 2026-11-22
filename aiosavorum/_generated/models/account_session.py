from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="AccountSession")



@_attrs_define
class AccountSession:
    """ 
        Attributes:
            auth_method (str):
            browser_handoff (bool): True when a native app created the session by exchanging a browser sign-in.
            created_at (datetime.datetime):
            current (bool):
            id (str):
            last_seen_at (datetime.datetime):
     """

    auth_method: str
    browser_handoff: bool
    created_at: datetime.datetime
    current: bool
    id: str
    last_seen_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        auth_method = self.auth_method

        browser_handoff = self.browser_handoff

        created_at = self.created_at.isoformat()

        current = self.current

        id = self.id

        last_seen_at = self.last_seen_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "auth_method": auth_method,
            "browser_handoff": browser_handoff,
            "created_at": created_at,
            "current": current,
            "id": id,
            "last_seen_at": last_seen_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_method = d.pop("auth_method")

        browser_handoff = d.pop("browser_handoff")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        current = d.pop("current")

        id = d.pop("id")

        last_seen_at = datetime.datetime.fromisoformat(d.pop("last_seen_at"))




        account_session = cls(
            auth_method=auth_method,
            browser_handoff=browser_handoff,
            created_at=created_at,
            current=current,
            id=id,
            last_seen_at=last_seen_at,
        )


        account_session.additional_properties = d
        return account_session

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
