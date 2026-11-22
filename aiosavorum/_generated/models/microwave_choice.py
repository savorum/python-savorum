from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.duration_expression import DurationExpression
  from ..models.microwave_power import MicrowavePower





T = TypeVar("T", bound="MicrowaveChoice")



@_attrs_define
class MicrowaveChoice:
    """ 
        Attributes:
            duration (DurationExpression):
            source_text (str):
            power (MicrowavePower | Unset):
            rated_output_watts (int | Unset):
     """

    duration: DurationExpression
    source_text: str
    power: MicrowavePower | Unset = UNSET
    rated_output_watts: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.duration_expression import DurationExpression # noqa: PLC0415
        from ..models.microwave_power import MicrowavePower # noqa: PLC0415
        duration = self.duration.to_dict()

        source_text = self.source_text

        power: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power, Unset):
            power = self.power.to_dict()

        rated_output_watts = self.rated_output_watts


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "duration": duration,
            "source_text": source_text,
        })
        if power is not UNSET:
            field_dict["power"] = power
        if rated_output_watts is not UNSET:
            field_dict["rated_output_watts"] = rated_output_watts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duration_expression import DurationExpression # noqa: PLC0415
        from ..models.microwave_power import MicrowavePower # noqa: PLC0415
        d = dict(src_dict)
        duration = DurationExpression.from_dict(d.pop("duration"))




        source_text = d.pop("source_text")

        _power = d.pop("power", UNSET)
        power: MicrowavePower | Unset
        if isinstance(_power,  Unset):
            power = UNSET
        else:
            power = MicrowavePower.from_dict(_power)




        rated_output_watts = d.pop("rated_output_watts", UNSET)

        microwave_choice = cls(
            duration=duration,
            source_text=source_text,
            power=power,
            rated_output_watts=rated_output_watts,
        )

        return microwave_choice

