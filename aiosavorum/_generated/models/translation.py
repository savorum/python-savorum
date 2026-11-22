from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.translation_relation import TranslationRelation
from ..types import UNSET, Unset






T = TypeVar("T", bound="Translation")



@_attrs_define
class Translation:
    """ 
        Attributes:
            language (str): The counterpart's primary language as a BCP 47 tag
            relation (TranslationRelation): original: this recipe was translated from the counterpart; translation: the
                counterpart was translated from this recipe; alternate: the same recipe in another language with no stated
                direction
            recipe_id (str | Unset): The counterpart's portable recipe document ID, not a library entry ID
            title (str | Unset): The counterpart's title as authored
            url (str | Unset): Where the counterpart is published
     """

    language: str
    relation: TranslationRelation
    recipe_id: str | Unset = UNSET
    title: str | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        language = self.language

        relation = self.relation.value

        recipe_id = self.recipe_id

        title = self.title

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "language": language,
            "relation": relation,
        })
        if recipe_id is not UNSET:
            field_dict["recipe_id"] = recipe_id
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language")

        relation = TranslationRelation(d.pop("relation"))




        recipe_id = d.pop("recipe_id", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        translation = cls(
            language=language,
            relation=relation,
            recipe_id=recipe_id,
            title=title,
            url=url,
        )

        return translation

