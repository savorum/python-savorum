from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.nutrition_basis_kind import NutritionBasisKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.quantity import Quantity





T = TypeVar("T", bound="NutritionBasis")



@_attrs_define
class NutritionBasis:
    """ 
        Attributes:
            kind (NutritionBasisKind): recipe: the whole recipe as written; serving: one serving; quantity: a stated amount
                such as 100 g; unspecified: the source did not say
            quantity (Quantity | Unset):
            text (str | Unset): Authored basis wording such as 1 slice
     """

    kind: NutritionBasisKind
    quantity: Quantity | Unset = UNSET
    text: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.quantity import Quantity # noqa: PLC0415
        kind = self.kind.value

        quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quantity, Unset):
            quantity = self.quantity.to_dict()

        text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quantity import Quantity # noqa: PLC0415
        d = dict(src_dict)
        kind = NutritionBasisKind(d.pop("kind"))




        _quantity = d.pop("quantity", UNSET)
        quantity: Quantity | Unset
        if isinstance(_quantity,  Unset):
            quantity = UNSET
        else:
            quantity = Quantity.from_dict(_quantity)




        text = d.pop("text", UNSET)

        nutrition_basis = cls(
            kind=kind,
            quantity=quantity,
            text=text,
        )

        return nutrition_basis

