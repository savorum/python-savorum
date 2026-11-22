from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.nutrient_nutrient import NutrientNutrient
from ..models.nutrient_unit import NutrientUnit
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.amount import Amount





T = TypeVar("T", bound="Nutrient")



@_attrs_define
class Nutrient:
    """ 
        Attributes:
            nutrient (NutrientNutrient):
            amount (Amount | Unset):
            label (str | Unset): The source's own name; required for other
            source_text (str | Unset):
            text (str | Unset): Wording that is not a precise value; excludes amount and unit
            unit (NutrientUnit | Unset): Absent when the source stated no unit
     """

    nutrient: NutrientNutrient
    amount: Amount | Unset = UNSET
    label: str | Unset = UNSET
    source_text: str | Unset = UNSET
    text: str | Unset = UNSET
    unit: NutrientUnit | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.amount import Amount # noqa: PLC0415
        nutrient = self.nutrient.value

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        label = self.label

        source_text = self.source_text

        text = self.text

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "nutrient": nutrient,
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if label is not UNSET:
            field_dict["label"] = label
        if source_text is not UNSET:
            field_dict["source_text"] = source_text
        if text is not UNSET:
            field_dict["text"] = text
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount import Amount # noqa: PLC0415
        d = dict(src_dict)
        nutrient = NutrientNutrient(d.pop("nutrient"))




        _amount = d.pop("amount", UNSET)
        amount: Amount | Unset
        if isinstance(_amount,  Unset):
            amount = UNSET
        else:
            amount = Amount.from_dict(_amount)




        label = d.pop("label", UNSET)

        source_text = d.pop("source_text", UNSET)

        text = d.pop("text", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: NutrientUnit | Unset
        if isinstance(_unit,  Unset):
            unit = UNSET
        else:
            unit = NutrientUnit(_unit)




        nutrient = cls(
            nutrient=nutrient,
            amount=amount,
            label=label,
            source_text=source_text,
            text=text,
            unit=unit,
        )

        return nutrient

