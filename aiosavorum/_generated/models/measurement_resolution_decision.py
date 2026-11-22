from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.measurement_resolution_choice import MeasurementResolutionChoice
  from ..models.measurement_resolution_example import MeasurementResolutionExample





T = TypeVar("T", bound="MeasurementResolutionDecision")



@_attrs_define
class MeasurementResolutionDecision:
    """ 
        Attributes:
            authored_forms (list[str] | None):
            candidate_unit_ids (list[str] | None):
            choices (list[MeasurementResolutionChoice] | None):
            examples (list[MeasurementResolutionExample] | None):
            group_ids (list[str] | None):
            id (str):
            ingredients (int):
            measure_label (str):
            occurrences (int):
            recipes (int):
            source_label (str | Unset):
     """

    authored_forms: list[str] | None
    candidate_unit_ids: list[str] | None
    choices: list[MeasurementResolutionChoice] | None
    examples: list[MeasurementResolutionExample] | None
    group_ids: list[str] | None
    id: str
    ingredients: int
    measure_label: str
    occurrences: int
    recipes: int
    source_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_resolution_choice import MeasurementResolutionChoice # noqa: PLC0415
        from ..models.measurement_resolution_example import MeasurementResolutionExample # noqa: PLC0415
        authored_forms: list[str] | None
        if isinstance(self.authored_forms, list):
            authored_forms = self.authored_forms


        else:
            authored_forms = self.authored_forms

        candidate_unit_ids: list[str] | None
        if isinstance(self.candidate_unit_ids, list):
            candidate_unit_ids = self.candidate_unit_ids


        else:
            candidate_unit_ids = self.candidate_unit_ids

        choices: list[dict[str, Any]] | None
        if isinstance(self.choices, list):
            choices = []
            for choices_type_0_item_data in self.choices:
                choices_type_0_item = choices_type_0_item_data.to_dict()
                choices.append(choices_type_0_item)


        else:
            choices = self.choices

        examples: list[dict[str, Any]] | None
        if isinstance(self.examples, list):
            examples = []
            for examples_type_0_item_data in self.examples:
                examples_type_0_item = examples_type_0_item_data.to_dict()
                examples.append(examples_type_0_item)


        else:
            examples = self.examples

        group_ids: list[str] | None
        if isinstance(self.group_ids, list):
            group_ids = self.group_ids


        else:
            group_ids = self.group_ids

        id = self.id

        ingredients = self.ingredients

        measure_label = self.measure_label

        occurrences = self.occurrences

        recipes = self.recipes

        source_label = self.source_label


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "authored_forms": authored_forms,
            "candidate_unit_ids": candidate_unit_ids,
            "choices": choices,
            "examples": examples,
            "group_ids": group_ids,
            "id": id,
            "ingredients": ingredients,
            "measure_label": measure_label,
            "occurrences": occurrences,
            "recipes": recipes,
        })
        if source_label is not UNSET:
            field_dict["source_label"] = source_label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_resolution_choice import MeasurementResolutionChoice # noqa: PLC0415
        from ..models.measurement_resolution_example import MeasurementResolutionExample # noqa: PLC0415
        d = dict(src_dict)
        def _parse_authored_forms(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authored_forms_type_0 = cast(list[str], data)

                return authored_forms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        authored_forms = _parse_authored_forms(d.pop("authored_forms"))


        def _parse_candidate_unit_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                candidate_unit_ids_type_0 = cast(list[str], data)

                return candidate_unit_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        candidate_unit_ids = _parse_candidate_unit_ids(d.pop("candidate_unit_ids"))


        def _parse_choices(data: object) -> list[MeasurementResolutionChoice] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                choices_type_0 = []
                _choices_type_0 = data
                for choices_type_0_item_data in (_choices_type_0):
                    choices_type_0_item = MeasurementResolutionChoice.from_dict(choices_type_0_item_data)



                    choices_type_0.append(choices_type_0_item)

                return choices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionChoice] | None, data)

        choices = _parse_choices(d.pop("choices"))


        def _parse_examples(data: object) -> list[MeasurementResolutionExample] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                examples_type_0 = []
                _examples_type_0 = data
                for examples_type_0_item_data in (_examples_type_0):
                    examples_type_0_item = MeasurementResolutionExample.from_dict(examples_type_0_item_data)



                    examples_type_0.append(examples_type_0_item)

                return examples_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionExample] | None, data)

        examples = _parse_examples(d.pop("examples"))


        def _parse_group_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        group_ids = _parse_group_ids(d.pop("group_ids"))


        id = d.pop("id")

        ingredients = d.pop("ingredients")

        measure_label = d.pop("measure_label")

        occurrences = d.pop("occurrences")

        recipes = d.pop("recipes")

        source_label = d.pop("source_label", UNSET)

        measurement_resolution_decision = cls(
            authored_forms=authored_forms,
            candidate_unit_ids=candidate_unit_ids,
            choices=choices,
            examples=examples,
            group_ids=group_ids,
            id=id,
            ingredients=ingredients,
            measure_label=measure_label,
            occurrences=occurrences,
            recipes=recipes,
            source_label=source_label,
        )


        measurement_resolution_decision.additional_properties = d
        return measurement_resolution_decision

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
