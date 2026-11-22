from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.microwave_choice import MicrowaveChoice
  from ..models.microwave_power import MicrowavePower





T = TypeVar("T", bound="MicrowaveConditions")



@_attrs_define
class MicrowaveConditions:
    """ 
        Attributes:
            source_text (str):
            choices (list[MicrowaveChoice] | None | Unset):
            mode_text (str | Unset):
            power (MicrowavePower | Unset):
            rated_output_watts (int | Unset):
            restrictions (list[str] | None | Unset):
     """

    source_text: str
    choices: list[MicrowaveChoice] | None | Unset = UNSET
    mode_text: str | Unset = UNSET
    power: MicrowavePower | Unset = UNSET
    rated_output_watts: int | Unset = UNSET
    restrictions: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.microwave_choice import MicrowaveChoice # noqa: PLC0415
        from ..models.microwave_power import MicrowavePower # noqa: PLC0415
        source_text = self.source_text

        choices: list[dict[str, Any]] | None | Unset
        if isinstance(self.choices, Unset):
            choices = UNSET
        elif isinstance(self.choices, list):
            choices = []
            for choices_type_0_item_data in self.choices:
                choices_type_0_item = choices_type_0_item_data.to_dict()
                choices.append(choices_type_0_item)


        else:
            choices = self.choices

        mode_text = self.mode_text

        power: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power, Unset):
            power = self.power.to_dict()

        rated_output_watts = self.rated_output_watts

        restrictions: list[str] | None | Unset
        if isinstance(self.restrictions, Unset):
            restrictions = UNSET
        elif isinstance(self.restrictions, list):
            restrictions = self.restrictions


        else:
            restrictions = self.restrictions


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "source_text": source_text,
        })
        if choices is not UNSET:
            field_dict["choices"] = choices
        if mode_text is not UNSET:
            field_dict["mode_text"] = mode_text
        if power is not UNSET:
            field_dict["power"] = power
        if rated_output_watts is not UNSET:
            field_dict["rated_output_watts"] = rated_output_watts
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.microwave_choice import MicrowaveChoice # noqa: PLC0415
        from ..models.microwave_power import MicrowavePower # noqa: PLC0415
        d = dict(src_dict)
        source_text = d.pop("source_text")

        def _parse_choices(data: object) -> list[MicrowaveChoice] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                choices_type_0 = []
                _choices_type_0 = data
                for choices_type_0_item_data in (_choices_type_0):
                    choices_type_0_item = MicrowaveChoice.from_dict(choices_type_0_item_data)



                    choices_type_0.append(choices_type_0_item)

                return choices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MicrowaveChoice] | None | Unset, data)

        choices = _parse_choices(d.pop("choices", UNSET))


        mode_text = d.pop("mode_text", UNSET)

        _power = d.pop("power", UNSET)
        power: MicrowavePower | Unset
        if isinstance(_power,  Unset):
            power = UNSET
        else:
            power = MicrowavePower.from_dict(_power)




        rated_output_watts = d.pop("rated_output_watts", UNSET)

        def _parse_restrictions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                restrictions_type_0 = cast(list[str], data)

                return restrictions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        restrictions = _parse_restrictions(d.pop("restrictions", UNSET))


        microwave_conditions = cls(
            source_text=source_text,
            choices=choices,
            mode_text=mode_text,
            power=power,
            rated_output_watts=rated_output_watts,
            restrictions=restrictions,
        )

        return microwave_conditions

