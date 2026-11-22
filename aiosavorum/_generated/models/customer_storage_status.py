from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.customer_storage_status_state import CustomerStorageStatusState
from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomerStorageStatus")



@_attrs_define
class CustomerStorageStatus:
    """ 
        Attributes:
            hosted (bool):
            state (CustomerStorageStatusState):
            available_bytes (int | Unset):
            available_inodes (int | Unset):
            limit_bytes (int | Unset):
            support_url (str | Unset):
            used_bytes (int | Unset):
     """

    hosted: bool
    state: CustomerStorageStatusState
    available_bytes: int | Unset = UNSET
    available_inodes: int | Unset = UNSET
    limit_bytes: int | Unset = UNSET
    support_url: str | Unset = UNSET
    used_bytes: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hosted = self.hosted

        state = self.state.value

        available_bytes = self.available_bytes

        available_inodes = self.available_inodes

        limit_bytes = self.limit_bytes

        support_url = self.support_url

        used_bytes = self.used_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "hosted": hosted,
            "state": state,
        })
        if available_bytes is not UNSET:
            field_dict["available_bytes"] = available_bytes
        if available_inodes is not UNSET:
            field_dict["available_inodes"] = available_inodes
        if limit_bytes is not UNSET:
            field_dict["limit_bytes"] = limit_bytes
        if support_url is not UNSET:
            field_dict["support_url"] = support_url
        if used_bytes is not UNSET:
            field_dict["used_bytes"] = used_bytes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hosted = d.pop("hosted")

        state = CustomerStorageStatusState(d.pop("state"))




        available_bytes = d.pop("available_bytes", UNSET)

        available_inodes = d.pop("available_inodes", UNSET)

        limit_bytes = d.pop("limit_bytes", UNSET)

        support_url = d.pop("support_url", UNSET)

        used_bytes = d.pop("used_bytes", UNSET)

        customer_storage_status = cls(
            hosted=hosted,
            state=state,
            available_bytes=available_bytes,
            available_inodes=available_inodes,
            limit_bytes=limit_bytes,
            support_url=support_url,
            used_bytes=used_bytes,
        )

        return customer_storage_status

