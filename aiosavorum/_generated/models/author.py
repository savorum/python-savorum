from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.author_kind import AuthorKind
from ..types import UNSET, Unset






T = TypeVar("T", bound="Author")



@_attrs_define
class Author:
    """ 
        Attributes:
            name (str):
            kind (AuthorKind | Unset): Absent when the source does not support a defensible classification
            kind_label (str | Unset): Source-authored classification used only with kind other
            url (str | Unset):
     """

    name: str
    kind: AuthorKind | Unset = UNSET
    kind_label: str | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        kind_label = self.kind_label

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if kind_label is not UNSET:
            field_dict["kind_label"] = kind_label
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _kind = d.pop("kind", UNSET)
        kind: AuthorKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = AuthorKind(_kind)




        kind_label = d.pop("kind_label", UNSET)

        url = d.pop("url", UNSET)

        author = cls(
            name=name,
            kind=kind,
            kind_label=kind_label,
            url=url,
        )

        return author

