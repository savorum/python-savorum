from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.setup_version import SetupVersion






T = TypeVar("T", bound="Setup")



@_attrs_define
class Setup:
    """ 
        Attributes:
            credential (str):
            instance (str):
            relay (str):
            remote_origin (str):
            version (SetupVersion):
     """

    credential: str
    instance: str
    relay: str
    remote_origin: str
    version: SetupVersion





    def to_dict(self) -> dict[str, Any]:
        credential = self.credential

        instance = self.instance

        relay = self.relay

        remote_origin = self.remote_origin

        version = self.version.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "credential": credential,
            "instance": instance,
            "relay": relay,
            "remote_origin": remote_origin,
            "version": version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential = d.pop("credential")

        instance = d.pop("instance")

        relay = d.pop("relay")

        remote_origin = d.pop("remote_origin")

        version = SetupVersion(d.pop("version"))




        setup = cls(
            credential=credential,
            instance=instance,
            relay=relay,
            remote_origin=remote_origin,
            version=version,
        )

        return setup

