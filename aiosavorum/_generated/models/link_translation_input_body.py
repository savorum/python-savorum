from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.link_translation_input_body_relation import LinkTranslationInputBodyRelation






T = TypeVar("T", bound="LinkTranslationInputBody")



@_attrs_define
class LinkTranslationInputBody:
    """ 
        Attributes:
            counterpart (str): Library entry of the other rendition
            relation (LinkTranslationInputBodyRelation): How the counterpart relates to this recipe
     """

    counterpart: str
    relation: LinkTranslationInputBodyRelation





    def to_dict(self) -> dict[str, Any]:
        counterpart = self.counterpart

        relation = self.relation.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "counterpart": counterpart,
            "relation": relation,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        counterpart = d.pop("counterpart")

        relation = LinkTranslationInputBodyRelation(d.pop("relation"))




        link_translation_input_body = cls(
            counterpart=counterpart,
            relation=relation,
        )

        return link_translation_input_body

