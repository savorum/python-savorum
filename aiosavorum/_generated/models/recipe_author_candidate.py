from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.recipe_author_candidate_match import RecipeAuthorCandidateMatch






T = TypeVar("T", bound="RecipeAuthorCandidate")



@_attrs_define
class RecipeAuthorCandidate:
    """ 
        Attributes:
            match (RecipeAuthorCandidateMatch): Best available tier: exact normalized name, Latin accent variant, or one
                edit or adjacent transposition
            name (str): Original author name to quote in an author: qualifier
            recipe_count (int): Active recipes with this exact credited spelling in the selected library
     """

    match: RecipeAuthorCandidateMatch
    name: str
    recipe_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        match = self.match.value

        name = self.name

        recipe_count = self.recipe_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "match": match,
            "name": name,
            "recipe_count": recipe_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match = RecipeAuthorCandidateMatch(d.pop("match"))




        name = d.pop("name")

        recipe_count = d.pop("recipe_count")

        recipe_author_candidate = cls(
            match=match,
            name=name,
            recipe_count=recipe_count,
        )


        recipe_author_candidate.additional_properties = d
        return recipe_author_candidate

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
