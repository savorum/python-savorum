from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.ingredient import Ingredient





T = TypeVar("T", bound="ParseIngredientLineOutputBody")



@_attrs_define
class ParseIngredientLineOutputBody:
    """ 
        Attributes:
            ingredient (Ingredient):
     """

    ingredient: Ingredient
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ingredient import Ingredient # noqa: PLC0415
        ingredient = self.ingredient.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ingredient": ingredient,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingredient import Ingredient # noqa: PLC0415
        d = dict(src_dict)
        ingredient = Ingredient.from_dict(d.pop("ingredient"))




        parse_ingredient_line_output_body = cls(
            ingredient=ingredient,
        )


        parse_ingredient_line_output_body.additional_properties = d
        return parse_ingredient_line_output_body

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
