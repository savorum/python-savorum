from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Source")



@_attrs_define
class Source:
    """ 
        Attributes:
            application (str | Unset): Portable source application or format identity; namespaces source_id
            attribution (str | Unset): Portable source credit or attribution
            name (str | Unset): Portable source name credited by the recipe
            retrieved_at (datetime.datetime | Unset): Supplementary retrieval time; does not identify a source
            source_id (str | Unset): Identifier within application; never a Savorum library or publication ID
            url (str | Unset): Portable canonical source URL
     """

    application: str | Unset = UNSET
    attribution: str | Unset = UNSET
    name: str | Unset = UNSET
    retrieved_at: datetime.datetime | Unset = UNSET
    source_id: str | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        application = self.application

        attribution = self.attribution

        name = self.name

        retrieved_at: str | Unset = UNSET
        if not isinstance(self.retrieved_at, Unset):
            retrieved_at = self.retrieved_at.isoformat()

        source_id = self.source_id

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if application is not UNSET:
            field_dict["application"] = application
        if attribution is not UNSET:
            field_dict["attribution"] = attribution
        if name is not UNSET:
            field_dict["name"] = name
        if retrieved_at is not UNSET:
            field_dict["retrieved_at"] = retrieved_at
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application = d.pop("application", UNSET)

        attribution = d.pop("attribution", UNSET)

        name = d.pop("name", UNSET)

        _retrieved_at = d.pop("retrieved_at", UNSET)
        retrieved_at: datetime.datetime | Unset
        if isinstance(_retrieved_at,  Unset):
            retrieved_at = UNSET
        else:
            retrieved_at = datetime.datetime.fromisoformat(_retrieved_at)




        source_id = d.pop("source_id", UNSET)

        url = d.pop("url", UNSET)

        source = cls(
            application=application,
            attribution=attribution,
            name=name,
            retrieved_at=retrieved_at,
            source_id=source_id,
            url=url,
        )

        return source

