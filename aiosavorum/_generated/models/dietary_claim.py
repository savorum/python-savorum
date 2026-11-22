from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dietary_claim_diet import DietaryClaimDiet
from ..models.dietary_claim_suitability import DietaryClaimSuitability
from ..types import UNSET, Unset






T = TypeVar("T", bound="DietaryClaim")



@_attrs_define
class DietaryClaim:
    """ 
        Attributes:
            suitability (DietaryClaimSuitability):
            text (str): The complete authored statement
            condition (str | Unset): Authored limit on the claim; a conditional claim is never shown or filtered as
                unconditional
            diet (DietaryClaimDiet | Unset): Normalized subject; absent when the diet has none
            variant_ref (str | Unset): The variant the claim describes, which it does not extend to the recipe as written
     """

    suitability: DietaryClaimSuitability
    text: str
    condition: str | Unset = UNSET
    diet: DietaryClaimDiet | Unset = UNSET
    variant_ref: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        suitability = self.suitability.value

        text = self.text

        condition = self.condition

        diet: str | Unset = UNSET
        if not isinstance(self.diet, Unset):
            diet = self.diet.value


        variant_ref = self.variant_ref


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "suitability": suitability,
            "text": text,
        })
        if condition is not UNSET:
            field_dict["condition"] = condition
        if diet is not UNSET:
            field_dict["diet"] = diet
        if variant_ref is not UNSET:
            field_dict["variant_ref"] = variant_ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suitability = DietaryClaimSuitability(d.pop("suitability"))




        text = d.pop("text")

        condition = d.pop("condition", UNSET)

        _diet = d.pop("diet", UNSET)
        diet: DietaryClaimDiet | Unset
        if isinstance(_diet,  Unset):
            diet = UNSET
        else:
            diet = DietaryClaimDiet(_diet)




        variant_ref = d.pop("variant_ref", UNSET)

        dietary_claim = cls(
            suitability=suitability,
            text=text,
            condition=condition,
            diet=diet,
            variant_ref=variant_ref,
        )

        return dietary_claim

