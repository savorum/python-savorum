from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.step import Step





T = TypeVar("T", bound="InstructionSection")



@_attrs_define
class InstructionSection:
    """ 
        Attributes:
            id (str):
            steps (list[Step] | None):
            title (str | Unset):
     """

    id: str
    steps: list[Step] | None
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.step import Step # noqa: PLC0415
        id = self.id

        steps: list[dict[str, Any]] | None
        if isinstance(self.steps, list):
            steps = []
            for steps_type_0_item_data in self.steps:
                steps_type_0_item = steps_type_0_item_data.to_dict()
                steps.append(steps_type_0_item)


        else:
            steps = self.steps

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "steps": steps,
        })
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step import Step # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_steps(data: object) -> list[Step] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                steps_type_0 = []
                _steps_type_0 = data
                for steps_type_0_item_data in (_steps_type_0):
                    steps_type_0_item = Step.from_dict(steps_type_0_item_data)



                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Step] | None, data)

        steps = _parse_steps(d.pop("steps"))


        title = d.pop("title", UNSET)

        instruction_section = cls(
            id=id,
            steps=steps,
            title=title,
        )

        return instruction_section

