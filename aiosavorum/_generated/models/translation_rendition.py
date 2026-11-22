from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.translation_rendition_relation import TranslationRenditionRelation






T = TypeVar("T", bound="TranslationRendition")



@_attrs_define
class TranslationRendition:
    """ 
        Attributes:
            id (str): Library entry identifier
            language (str): BCP 47 tag of the rendition's primary language
            linked (bool): One of the two recipes names the other, so the relationship can be removed from either
            relation (TranslationRenditionRelation): How the rendition relates to the requested recipe
            title (str):
     """

    id: str
    language: str
    linked: bool
    relation: TranslationRenditionRelation
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        language = self.language

        linked = self.linked

        relation = self.relation.value

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "language": language,
            "linked": linked,
            "relation": relation,
            "title": title,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        language = d.pop("language")

        linked = d.pop("linked")

        relation = TranslationRenditionRelation(d.pop("relation"))




        title = d.pop("title")

        translation_rendition = cls(
            id=id,
            language=language,
            linked=linked,
            relation=relation,
            title=title,
        )


        translation_rendition.additional_properties = d
        return translation_rendition

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
