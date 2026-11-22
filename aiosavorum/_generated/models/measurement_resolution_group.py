from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.measurement_resolution_group_kind import MeasurementResolutionGroupKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.measurement_resolution_choice import MeasurementResolutionChoice
  from ..models.measurement_resolution_example import MeasurementResolutionExample
  from ..models.measurement_resolution_subgroup import MeasurementResolutionSubgroup





T = TypeVar("T", bound="MeasurementResolutionGroup")



@_attrs_define
class MeasurementResolutionGroup:
    """ 
        Attributes:
            authored_form (str):
            candidate_unit_ids (list[str] | None):
            choices (list[MeasurementResolutionChoice] | None):
            examples (list[MeasurementResolutionExample] | None):
            id (str):
            ingredients (int):
            kind (MeasurementResolutionGroupKind):
            occurrences (int):
            recipes (int):
            subgroups (list[MeasurementResolutionSubgroup] | None):
            source_label (str | Unset):
     """

    authored_form: str
    candidate_unit_ids: list[str] | None
    choices: list[MeasurementResolutionChoice] | None
    examples: list[MeasurementResolutionExample] | None
    id: str
    ingredients: int
    kind: MeasurementResolutionGroupKind
    occurrences: int
    recipes: int
    subgroups: list[MeasurementResolutionSubgroup] | None
    source_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.measurement_resolution_choice import MeasurementResolutionChoice # noqa: PLC0415
        from ..models.measurement_resolution_example import MeasurementResolutionExample # noqa: PLC0415
        from ..models.measurement_resolution_subgroup import MeasurementResolutionSubgroup # noqa: PLC0415
        authored_form = self.authored_form

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

        id = self.id

        ingredients = self.ingredients

        kind = self.kind.value

        occurrences = self.occurrences

        recipes = self.recipes

        subgroups: list[dict[str, Any]] | None
        if isinstance(self.subgroups, list):
            subgroups = []
            for subgroups_type_0_item_data in self.subgroups:
                subgroups_type_0_item = subgroups_type_0_item_data.to_dict()
                subgroups.append(subgroups_type_0_item)


        else:
            subgroups = self.subgroups

        source_label = self.source_label


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "authored_form": authored_form,
            "candidate_unit_ids": candidate_unit_ids,
            "choices": choices,
            "examples": examples,
            "id": id,
            "ingredients": ingredients,
            "kind": kind,
            "occurrences": occurrences,
            "recipes": recipes,
            "subgroups": subgroups,
        })
        if source_label is not UNSET:
            field_dict["source_label"] = source_label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_resolution_choice import MeasurementResolutionChoice # noqa: PLC0415
        from ..models.measurement_resolution_example import MeasurementResolutionExample # noqa: PLC0415
        from ..models.measurement_resolution_subgroup import MeasurementResolutionSubgroup # noqa: PLC0415
        d = dict(src_dict)
        authored_form = d.pop("authored_form")

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


        id = d.pop("id")

        ingredients = d.pop("ingredients")

        kind = MeasurementResolutionGroupKind(d.pop("kind"))




        occurrences = d.pop("occurrences")

        recipes = d.pop("recipes")

        def _parse_subgroups(data: object) -> list[MeasurementResolutionSubgroup] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subgroups_type_0 = []
                _subgroups_type_0 = data
                for subgroups_type_0_item_data in (_subgroups_type_0):
                    subgroups_type_0_item = MeasurementResolutionSubgroup.from_dict(subgroups_type_0_item_data)



                    subgroups_type_0.append(subgroups_type_0_item)

                return subgroups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionSubgroup] | None, data)

        subgroups = _parse_subgroups(d.pop("subgroups"))


        source_label = d.pop("source_label", UNSET)

        measurement_resolution_group = cls(
            authored_form=authored_form,
            candidate_unit_ids=candidate_unit_ids,
            choices=choices,
            examples=examples,
            id=id,
            ingredients=ingredients,
            kind=kind,
            occurrences=occurrences,
            recipes=recipes,
            subgroups=subgroups,
            source_label=source_label,
        )


        measurement_resolution_group.additional_properties = d
        return measurement_resolution_group

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
