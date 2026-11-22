from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_preview_response import ImportPreviewResponse
  from ..models.measurement_resolution_example import MeasurementResolutionExample
  from ..models.measurement_resolution_occurrence import MeasurementResolutionOccurrence





T = TypeVar("T", bound="MeasurementResolutionPlanResponse")



@_attrs_define
class MeasurementResolutionPlanResponse:
    """ 
        Attributes:
            affected_ingredients (int):
            affected_occurrences (int):
            affected_recipes (int):
            current_actionable_occurrences (int):
            examples (list[MeasurementResolutionExample] | None):
            impact_digest (str):
            occurrences (list[MeasurementResolutionOccurrence] | None):
            pending_occurrences (list[MeasurementResolutionOccurrence] | None):
            plan_id (str):
            preview_revision (int):
            remaining_actionable_occurrences (int):
            resulting_actionable_occurrences (int):
            unchanged_occurrences (int):
            unresolvable_occurrences (list[MeasurementResolutionOccurrence] | None):
            validation_failures (list[str] | None):
            preview (ImportPreviewResponse | Unset):
     """

    affected_ingredients: int
    affected_occurrences: int
    affected_recipes: int
    current_actionable_occurrences: int
    examples: list[MeasurementResolutionExample] | None
    impact_digest: str
    occurrences: list[MeasurementResolutionOccurrence] | None
    pending_occurrences: list[MeasurementResolutionOccurrence] | None
    plan_id: str
    preview_revision: int
    remaining_actionable_occurrences: int
    resulting_actionable_occurrences: int
    unchanged_occurrences: int
    unresolvable_occurrences: list[MeasurementResolutionOccurrence] | None
    validation_failures: list[str] | None
    preview: ImportPreviewResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_preview_response import ImportPreviewResponse # noqa: PLC0415
        from ..models.measurement_resolution_example import MeasurementResolutionExample # noqa: PLC0415
        from ..models.measurement_resolution_occurrence import MeasurementResolutionOccurrence # noqa: PLC0415
        affected_ingredients = self.affected_ingredients

        affected_occurrences = self.affected_occurrences

        affected_recipes = self.affected_recipes

        current_actionable_occurrences = self.current_actionable_occurrences

        examples: list[dict[str, Any]] | None
        if isinstance(self.examples, list):
            examples = []
            for examples_type_0_item_data in self.examples:
                examples_type_0_item = examples_type_0_item_data.to_dict()
                examples.append(examples_type_0_item)


        else:
            examples = self.examples

        impact_digest = self.impact_digest

        occurrences: list[dict[str, Any]] | None
        if isinstance(self.occurrences, list):
            occurrences = []
            for occurrences_type_0_item_data in self.occurrences:
                occurrences_type_0_item = occurrences_type_0_item_data.to_dict()
                occurrences.append(occurrences_type_0_item)


        else:
            occurrences = self.occurrences

        pending_occurrences: list[dict[str, Any]] | None
        if isinstance(self.pending_occurrences, list):
            pending_occurrences = []
            for pending_occurrences_type_0_item_data in self.pending_occurrences:
                pending_occurrences_type_0_item = pending_occurrences_type_0_item_data.to_dict()
                pending_occurrences.append(pending_occurrences_type_0_item)


        else:
            pending_occurrences = self.pending_occurrences

        plan_id = self.plan_id

        preview_revision = self.preview_revision

        remaining_actionable_occurrences = self.remaining_actionable_occurrences

        resulting_actionable_occurrences = self.resulting_actionable_occurrences

        unchanged_occurrences = self.unchanged_occurrences

        unresolvable_occurrences: list[dict[str, Any]] | None
        if isinstance(self.unresolvable_occurrences, list):
            unresolvable_occurrences = []
            for unresolvable_occurrences_type_0_item_data in self.unresolvable_occurrences:
                unresolvable_occurrences_type_0_item = unresolvable_occurrences_type_0_item_data.to_dict()
                unresolvable_occurrences.append(unresolvable_occurrences_type_0_item)


        else:
            unresolvable_occurrences = self.unresolvable_occurrences

        validation_failures: list[str] | None
        if isinstance(self.validation_failures, list):
            validation_failures = self.validation_failures


        else:
            validation_failures = self.validation_failures

        preview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "affected_ingredients": affected_ingredients,
            "affected_occurrences": affected_occurrences,
            "affected_recipes": affected_recipes,
            "current_actionable_occurrences": current_actionable_occurrences,
            "examples": examples,
            "impact_digest": impact_digest,
            "occurrences": occurrences,
            "pending_occurrences": pending_occurrences,
            "plan_id": plan_id,
            "preview_revision": preview_revision,
            "remaining_actionable_occurrences": remaining_actionable_occurrences,
            "resulting_actionable_occurrences": resulting_actionable_occurrences,
            "unchanged_occurrences": unchanged_occurrences,
            "unresolvable_occurrences": unresolvable_occurrences,
            "validation_failures": validation_failures,
        })
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_preview_response import ImportPreviewResponse # noqa: PLC0415
        from ..models.measurement_resolution_example import MeasurementResolutionExample # noqa: PLC0415
        from ..models.measurement_resolution_occurrence import MeasurementResolutionOccurrence # noqa: PLC0415
        d = dict(src_dict)
        affected_ingredients = d.pop("affected_ingredients")

        affected_occurrences = d.pop("affected_occurrences")

        affected_recipes = d.pop("affected_recipes")

        current_actionable_occurrences = d.pop("current_actionable_occurrences")

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


        impact_digest = d.pop("impact_digest")

        def _parse_occurrences(data: object) -> list[MeasurementResolutionOccurrence] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                occurrences_type_0 = []
                _occurrences_type_0 = data
                for occurrences_type_0_item_data in (_occurrences_type_0):
                    occurrences_type_0_item = MeasurementResolutionOccurrence.from_dict(occurrences_type_0_item_data)



                    occurrences_type_0.append(occurrences_type_0_item)

                return occurrences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionOccurrence] | None, data)

        occurrences = _parse_occurrences(d.pop("occurrences"))


        def _parse_pending_occurrences(data: object) -> list[MeasurementResolutionOccurrence] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pending_occurrences_type_0 = []
                _pending_occurrences_type_0 = data
                for pending_occurrences_type_0_item_data in (_pending_occurrences_type_0):
                    pending_occurrences_type_0_item = MeasurementResolutionOccurrence.from_dict(pending_occurrences_type_0_item_data)



                    pending_occurrences_type_0.append(pending_occurrences_type_0_item)

                return pending_occurrences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionOccurrence] | None, data)

        pending_occurrences = _parse_pending_occurrences(d.pop("pending_occurrences"))


        plan_id = d.pop("plan_id")

        preview_revision = d.pop("preview_revision")

        remaining_actionable_occurrences = d.pop("remaining_actionable_occurrences")

        resulting_actionable_occurrences = d.pop("resulting_actionable_occurrences")

        unchanged_occurrences = d.pop("unchanged_occurrences")

        def _parse_unresolvable_occurrences(data: object) -> list[MeasurementResolutionOccurrence] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unresolvable_occurrences_type_0 = []
                _unresolvable_occurrences_type_0 = data
                for unresolvable_occurrences_type_0_item_data in (_unresolvable_occurrences_type_0):
                    unresolvable_occurrences_type_0_item = MeasurementResolutionOccurrence.from_dict(unresolvable_occurrences_type_0_item_data)



                    unresolvable_occurrences_type_0.append(unresolvable_occurrences_type_0_item)

                return unresolvable_occurrences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeasurementResolutionOccurrence] | None, data)

        unresolvable_occurrences = _parse_unresolvable_occurrences(d.pop("unresolvable_occurrences"))


        def _parse_validation_failures(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                validation_failures_type_0 = cast(list[str], data)

                return validation_failures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        validation_failures = _parse_validation_failures(d.pop("validation_failures"))


        _preview = d.pop("preview", UNSET)
        preview: ImportPreviewResponse | Unset
        if isinstance(_preview,  Unset):
            preview = UNSET
        else:
            preview = ImportPreviewResponse.from_dict(_preview)




        measurement_resolution_plan_response = cls(
            affected_ingredients=affected_ingredients,
            affected_occurrences=affected_occurrences,
            affected_recipes=affected_recipes,
            current_actionable_occurrences=current_actionable_occurrences,
            examples=examples,
            impact_digest=impact_digest,
            occurrences=occurrences,
            pending_occurrences=pending_occurrences,
            plan_id=plan_id,
            preview_revision=preview_revision,
            remaining_actionable_occurrences=remaining_actionable_occurrences,
            resulting_actionable_occurrences=resulting_actionable_occurrences,
            unchanged_occurrences=unchanged_occurrences,
            unresolvable_occurrences=unresolvable_occurrences,
            validation_failures=validation_failures,
            preview=preview,
        )


        measurement_resolution_plan_response.additional_properties = d
        return measurement_resolution_plan_response

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
