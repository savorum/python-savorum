from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.parse_ingredient_line_input_body_convention import ParseIngredientLineInputBodyConvention
from ..types import UNSET, Unset






T = TypeVar("T", bound="ParseIngredientLineInputBody")



@_attrs_define
class ParseIngredientLineInputBody:
    """ 
        Attributes:
            text (str): One ingredient line as a person writes it, such as 2 cups flour, sifted or 小麦粉 200g
            convention (ParseIngredientLineInputBodyConvention | Unset): An explicit author choice for every applicable
                unqualified measure of this submitted ingredient line. It outranks source-locale lookup and preserves explicit
                unit definitions. Omit it when unspecified
            language (str | Unset): BCP 47 tag of the language the line is written in. Its primary language selects unit
                words and reading order; its region does not establish a measuring convention
            source_locale (str | Unset): BCP 47 tag of the locale the recipe declares. It takes the place of language when
                the two are sent
     """

    text: str
    convention: ParseIngredientLineInputBodyConvention | Unset = UNSET
    language: str | Unset = UNSET
    source_locale: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        text = self.text

        convention: str | Unset = UNSET
        if not isinstance(self.convention, Unset):
            convention = self.convention.value


        language = self.language

        source_locale = self.source_locale


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
        })
        if convention is not UNSET:
            field_dict["convention"] = convention
        if language is not UNSET:
            field_dict["language"] = language
        if source_locale is not UNSET:
            field_dict["source_locale"] = source_locale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        _convention = d.pop("convention", UNSET)
        convention: ParseIngredientLineInputBodyConvention | Unset
        if isinstance(_convention,  Unset):
            convention = UNSET
        else:
            convention = ParseIngredientLineInputBodyConvention(_convention)




        language = d.pop("language", UNSET)

        source_locale = d.pop("source_locale", UNSET)

        parse_ingredient_line_input_body = cls(
            text=text,
            convention=convention,
            language=language,
            source_locale=source_locale,
        )

        return parse_ingredient_line_input_body

