from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.allergen_declaration_presence import AllergenDeclarationPresence
from ..types import UNSET, Unset






T = TypeVar("T", bound="AllergenDeclaration")



@_attrs_define
class AllergenDeclaration:
    """ 
        Attributes:
            presence (AllergenDeclarationPresence): contains: present; may_contain: precautionary or cross-contact warning;
                free_from: explicit absence claim
            substance (str): The substance as the source names it
            text (str): The complete authored statement
            condition (str | Unset):
            variant_ref (str | Unset):
     """

    presence: AllergenDeclarationPresence
    substance: str
    text: str
    condition: str | Unset = UNSET
    variant_ref: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        presence = self.presence.value

        substance = self.substance

        text = self.text

        condition = self.condition

        variant_ref = self.variant_ref


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "presence": presence,
            "substance": substance,
            "text": text,
        })
        if condition is not UNSET:
            field_dict["condition"] = condition
        if variant_ref is not UNSET:
            field_dict["variant_ref"] = variant_ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        presence = AllergenDeclarationPresence(d.pop("presence"))




        substance = d.pop("substance")

        text = d.pop("text")

        condition = d.pop("condition", UNSET)

        variant_ref = d.pop("variant_ref", UNSET)

        allergen_declaration = cls(
            presence=presence,
            substance=substance,
            text=text,
            condition=condition,
            variant_ref=variant_ref,
        )

        return allergen_declaration

