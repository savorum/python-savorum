from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.shopping_choice import ShoppingChoice
  from ..models.shopping_source import ShoppingSource





T = TypeVar("T", bound="ShoppingRequirement")



@_attrs_define
class ShoppingRequirement:
    """ 
        Attributes:
            choice_id (str):
            choices (list[ShoppingChoice] | None):
            id (str):
            selected (bool):
            source (ShoppingSource):
            previous_name (str | Unset):
            previous_quantity (str | Unset):
            reviewed_at (datetime.datetime | Unset):
     """

    choice_id: str
    choices: list[ShoppingChoice] | None
    id: str
    selected: bool
    source: ShoppingSource
    previous_name: str | Unset = UNSET
    previous_quantity: str | Unset = UNSET
    reviewed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shopping_choice import ShoppingChoice # noqa: PLC0415
        from ..models.shopping_source import ShoppingSource # noqa: PLC0415
        choice_id = self.choice_id

        choices: list[dict[str, Any]] | None
        if isinstance(self.choices, list):
            choices = []
            for choices_type_0_item_data in self.choices:
                choices_type_0_item = choices_type_0_item_data.to_dict()
                choices.append(choices_type_0_item)


        else:
            choices = self.choices

        id = self.id

        selected = self.selected

        source = self.source.to_dict()

        previous_name = self.previous_name

        previous_quantity = self.previous_quantity

        reviewed_at: str | Unset = UNSET
        if not isinstance(self.reviewed_at, Unset):
            reviewed_at = self.reviewed_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "choice_id": choice_id,
            "choices": choices,
            "id": id,
            "selected": selected,
            "source": source,
        })
        if previous_name is not UNSET:
            field_dict["previous_name"] = previous_name
        if previous_quantity is not UNSET:
            field_dict["previous_quantity"] = previous_quantity
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shopping_choice import ShoppingChoice # noqa: PLC0415
        from ..models.shopping_source import ShoppingSource # noqa: PLC0415
        d = dict(src_dict)
        choice_id = d.pop("choice_id")

        def _parse_choices(data: object) -> list[ShoppingChoice] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                choices_type_0 = []
                _choices_type_0 = data
                for choices_type_0_item_data in (_choices_type_0):
                    choices_type_0_item = ShoppingChoice.from_dict(choices_type_0_item_data)



                    choices_type_0.append(choices_type_0_item)

                return choices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShoppingChoice] | None, data)

        choices = _parse_choices(d.pop("choices"))


        id = d.pop("id")

        selected = d.pop("selected")

        source = ShoppingSource.from_dict(d.pop("source"))




        previous_name = d.pop("previous_name", UNSET)

        previous_quantity = d.pop("previous_quantity", UNSET)

        _reviewed_at = d.pop("reviewed_at", UNSET)
        reviewed_at: datetime.datetime | Unset
        if isinstance(_reviewed_at,  Unset):
            reviewed_at = UNSET
        else:
            reviewed_at = datetime.datetime.fromisoformat(_reviewed_at)




        shopping_requirement = cls(
            choice_id=choice_id,
            choices=choices,
            id=id,
            selected=selected,
            source=source,
            previous_name=previous_name,
            previous_quantity=previous_quantity,
            reviewed_at=reviewed_at,
        )


        shopping_requirement.additional_properties = d
        return shopping_requirement

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
