from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Status")



@_attrs_define
class Status:
    """ 
        Attributes:
            certificate_ready (bool):
            configured (bool):
            state (str):
            certificate_expires (str | Unset):
            remote_origin (str | Unset):
     """

    certificate_ready: bool
    configured: bool
    state: str
    certificate_expires: str | Unset = UNSET
    remote_origin: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        certificate_ready = self.certificate_ready

        configured = self.configured

        state = self.state

        certificate_expires = self.certificate_expires

        remote_origin = self.remote_origin


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "certificate_ready": certificate_ready,
            "configured": configured,
            "state": state,
        })
        if certificate_expires is not UNSET:
            field_dict["certificate_expires"] = certificate_expires
        if remote_origin is not UNSET:
            field_dict["remote_origin"] = remote_origin

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate_ready = d.pop("certificate_ready")

        configured = d.pop("configured")

        state = d.pop("state")

        certificate_expires = d.pop("certificate_expires", UNSET)

        remote_origin = d.pop("remote_origin", UNSET)

        status = cls(
            certificate_ready=certificate_ready,
            configured=configured,
            state=state,
            certificate_expires=certificate_expires,
            remote_origin=remote_origin,
        )

        return status

