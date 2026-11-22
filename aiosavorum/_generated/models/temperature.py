from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.temperature_amount import TemperatureAmount
  from ..models.temperature_purpose import TemperaturePurpose





T = TypeVar("T", bound="Temperature")



@_attrs_define
class Temperature:
    """ 
        Attributes:
            amount (TemperatureAmount | Unset):
            note (str | Unset):
            purpose (TemperaturePurpose | Unset):
            source_text (str | Unset):
            text (str | Unset):
            unit (str | Unset):
     """

    amount: TemperatureAmount | Unset = UNSET
    note: str | Unset = UNSET
    purpose: TemperaturePurpose | Unset = UNSET
    source_text: str | Unset = UNSET
    text: str | Unset = UNSET
    unit: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.temperature_amount import TemperatureAmount # noqa: PLC0415
        from ..models.temperature_purpose import TemperaturePurpose # noqa: PLC0415
        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        note = self.note

        purpose: dict[str, Any] | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.to_dict()

        source_text = self.source_text

        text = self.text

        unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if note is not UNSET:
            field_dict["note"] = note
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if source_text is not UNSET:
            field_dict["source_text"] = source_text
        if text is not UNSET:
            field_dict["text"] = text
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.temperature_amount import TemperatureAmount # noqa: PLC0415
        from ..models.temperature_purpose import TemperaturePurpose # noqa: PLC0415
        d = dict(src_dict)
        _amount = d.pop("amount", UNSET)
        amount: TemperatureAmount | Unset
        if isinstance(_amount,  Unset):
            amount = UNSET
        else:
            amount = TemperatureAmount.from_dict(_amount)




        note = d.pop("note", UNSET)

        _purpose = d.pop("purpose", UNSET)
        purpose: TemperaturePurpose | Unset
        if isinstance(_purpose,  Unset):
            purpose = UNSET
        else:
            purpose = TemperaturePurpose.from_dict(_purpose)




        source_text = d.pop("source_text", UNSET)

        text = d.pop("text", UNSET)

        unit = d.pop("unit", UNSET)

        temperature = cls(
            amount=amount,
            note=note,
            purpose=purpose,
            source_text=source_text,
            text=text,
            unit=unit,
        )

        return temperature

