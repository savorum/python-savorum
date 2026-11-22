from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.quantity import Quantity





T = TypeVar("T", bound="IngredientUse")



@_attrs_define
class IngredientUse:
    """ 
        Attributes:
            ingredient_ref (str):
            quantity (Quantity | Unset):
     """

    ingredient_ref: str
    quantity: Quantity | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.quantity import Quantity # noqa: PLC0415
        ingredient_ref = self.ingredient_ref

        quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quantity, Unset):
            quantity = self.quantity.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ingredient_ref": ingredient_ref,
        })
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quantity import Quantity # noqa: PLC0415
        d = dict(src_dict)
        ingredient_ref = d.pop("ingredient_ref")

        _quantity = d.pop("quantity", UNSET)
        quantity: Quantity | Unset
        if isinstance(_quantity,  Unset):
            quantity = UNSET
        else:
            quantity = Quantity.from_dict(_quantity)




        ingredient_use = cls(
            ingredient_ref=ingredient_ref,
            quantity=quantity,
        )

        return ingredient_use

