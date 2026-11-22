from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.simple_quantity_kind import SimpleQuantityKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.amount import Amount





T = TypeVar("T", bound="SimpleQuantity")



@_attrs_define
class SimpleQuantity:
    """ 
        Attributes:
            amount (Amount):
            kind (SimpleQuantityKind):
            unit (str | Unset):
     """

    amount: Amount
    kind: SimpleQuantityKind
    unit: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.amount import Amount # noqa: PLC0415
        amount = self.amount.to_dict()

        kind = self.kind.value

        unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "amount": amount,
            "kind": kind,
        })
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount import Amount # noqa: PLC0415
        d = dict(src_dict)
        amount = Amount.from_dict(d.pop("amount"))




        kind = SimpleQuantityKind(d.pop("kind"))




        unit = d.pop("unit", UNSET)

        simple_quantity = cls(
            amount=amount,
            kind=kind,
            unit=unit,
        )

        return simple_quantity

