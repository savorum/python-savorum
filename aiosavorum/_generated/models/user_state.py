from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UserState")



@_attrs_define
class UserState:
    """ 
        Attributes:
            favorite (bool):
            personal_note (str | Unset):
            preferred_scale (str | Unset): Preferred batch as an exact factor, for a yield that is not a number
            preferred_yield (str | Unset): Preferred yield as an exact amount of the recipe's own yield
            preferred_yield_assertion (int | Unset): Position in the recipe's yields of the yield this reader shows first
                and scales by. It does not reorder the recipe's yields.
            rating (int | Unset):
     """

    favorite: bool
    personal_note: str | Unset = UNSET
    preferred_scale: str | Unset = UNSET
    preferred_yield: str | Unset = UNSET
    preferred_yield_assertion: int | Unset = UNSET
    rating: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        favorite = self.favorite

        personal_note = self.personal_note

        preferred_scale = self.preferred_scale

        preferred_yield = self.preferred_yield

        preferred_yield_assertion = self.preferred_yield_assertion

        rating = self.rating


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "favorite": favorite,
        })
        if personal_note is not UNSET:
            field_dict["personal_note"] = personal_note
        if preferred_scale is not UNSET:
            field_dict["preferred_scale"] = preferred_scale
        if preferred_yield is not UNSET:
            field_dict["preferred_yield"] = preferred_yield
        if preferred_yield_assertion is not UNSET:
            field_dict["preferred_yield_assertion"] = preferred_yield_assertion
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        favorite = d.pop("favorite")

        personal_note = d.pop("personal_note", UNSET)

        preferred_scale = d.pop("preferred_scale", UNSET)

        preferred_yield = d.pop("preferred_yield", UNSET)

        preferred_yield_assertion = d.pop("preferred_yield_assertion", UNSET)

        rating = d.pop("rating", UNSET)

        user_state = cls(
            favorite=favorite,
            personal_note=personal_note,
            preferred_scale=preferred_scale,
            preferred_yield=preferred_yield,
            preferred_yield_assertion=preferred_yield_assertion,
            rating=rating,
        )

        return user_state

