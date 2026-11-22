from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ImportResolutionDecision")



@_attrs_define
class ImportResolutionDecision:
    """ 
        Attributes:
            affected_ingredient_count (int):
            affected_occurrence_ids (list[str] | None):
            affected_recipe_count (int):
            decision_scope (str):
            impact_digest (str):
            interpretation_kind (str):
            original_actionable_count (int):
            parser_version (str):
            resolution_kind (str):
            resulting_actionable_count (int):
            unit_registry_version (str):
            convention (str | Unset):
            convention_unit_ids (list[str] | None | Unset):
            excluded_item_ids (list[str] | None | Unset):
            excluded_occurrence_ids (list[str] | None | Unset):
            scope_ingredient_ids (list[str] | None | Unset):
            scope_occurrence_keys (list[str] | None | Unset):
            unit_id (str | Unset):
     """

    affected_ingredient_count: int
    affected_occurrence_ids: list[str] | None
    affected_recipe_count: int
    decision_scope: str
    impact_digest: str
    interpretation_kind: str
    original_actionable_count: int
    parser_version: str
    resolution_kind: str
    resulting_actionable_count: int
    unit_registry_version: str
    convention: str | Unset = UNSET
    convention_unit_ids: list[str] | None | Unset = UNSET
    excluded_item_ids: list[str] | None | Unset = UNSET
    excluded_occurrence_ids: list[str] | None | Unset = UNSET
    scope_ingredient_ids: list[str] | None | Unset = UNSET
    scope_occurrence_keys: list[str] | None | Unset = UNSET
    unit_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        affected_ingredient_count = self.affected_ingredient_count

        affected_occurrence_ids: list[str] | None
        if isinstance(self.affected_occurrence_ids, list):
            affected_occurrence_ids = self.affected_occurrence_ids


        else:
            affected_occurrence_ids = self.affected_occurrence_ids

        affected_recipe_count = self.affected_recipe_count

        decision_scope = self.decision_scope

        impact_digest = self.impact_digest

        interpretation_kind = self.interpretation_kind

        original_actionable_count = self.original_actionable_count

        parser_version = self.parser_version

        resolution_kind = self.resolution_kind

        resulting_actionable_count = self.resulting_actionable_count

        unit_registry_version = self.unit_registry_version

        convention = self.convention

        convention_unit_ids: list[str] | None | Unset
        if isinstance(self.convention_unit_ids, Unset):
            convention_unit_ids = UNSET
        elif isinstance(self.convention_unit_ids, list):
            convention_unit_ids = self.convention_unit_ids


        else:
            convention_unit_ids = self.convention_unit_ids

        excluded_item_ids: list[str] | None | Unset
        if isinstance(self.excluded_item_ids, Unset):
            excluded_item_ids = UNSET
        elif isinstance(self.excluded_item_ids, list):
            excluded_item_ids = self.excluded_item_ids


        else:
            excluded_item_ids = self.excluded_item_ids

        excluded_occurrence_ids: list[str] | None | Unset
        if isinstance(self.excluded_occurrence_ids, Unset):
            excluded_occurrence_ids = UNSET
        elif isinstance(self.excluded_occurrence_ids, list):
            excluded_occurrence_ids = self.excluded_occurrence_ids


        else:
            excluded_occurrence_ids = self.excluded_occurrence_ids

        scope_ingredient_ids: list[str] | None | Unset
        if isinstance(self.scope_ingredient_ids, Unset):
            scope_ingredient_ids = UNSET
        elif isinstance(self.scope_ingredient_ids, list):
            scope_ingredient_ids = self.scope_ingredient_ids


        else:
            scope_ingredient_ids = self.scope_ingredient_ids

        scope_occurrence_keys: list[str] | None | Unset
        if isinstance(self.scope_occurrence_keys, Unset):
            scope_occurrence_keys = UNSET
        elif isinstance(self.scope_occurrence_keys, list):
            scope_occurrence_keys = self.scope_occurrence_keys


        else:
            scope_occurrence_keys = self.scope_occurrence_keys

        unit_id = self.unit_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "affected_ingredient_count": affected_ingredient_count,
            "affected_occurrence_ids": affected_occurrence_ids,
            "affected_recipe_count": affected_recipe_count,
            "decision_scope": decision_scope,
            "impact_digest": impact_digest,
            "interpretation_kind": interpretation_kind,
            "original_actionable_count": original_actionable_count,
            "parser_version": parser_version,
            "resolution_kind": resolution_kind,
            "resulting_actionable_count": resulting_actionable_count,
            "unit_registry_version": unit_registry_version,
        })
        if convention is not UNSET:
            field_dict["convention"] = convention
        if convention_unit_ids is not UNSET:
            field_dict["convention_unit_ids"] = convention_unit_ids
        if excluded_item_ids is not UNSET:
            field_dict["excluded_item_ids"] = excluded_item_ids
        if excluded_occurrence_ids is not UNSET:
            field_dict["excluded_occurrence_ids"] = excluded_occurrence_ids
        if scope_ingredient_ids is not UNSET:
            field_dict["scope_ingredient_ids"] = scope_ingredient_ids
        if scope_occurrence_keys is not UNSET:
            field_dict["scope_occurrence_keys"] = scope_occurrence_keys
        if unit_id is not UNSET:
            field_dict["unit_id"] = unit_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_ingredient_count = d.pop("affected_ingredient_count")

        def _parse_affected_occurrence_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                affected_occurrence_ids_type_0 = cast(list[str], data)

                return affected_occurrence_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        affected_occurrence_ids = _parse_affected_occurrence_ids(d.pop("affected_occurrence_ids"))


        affected_recipe_count = d.pop("affected_recipe_count")

        decision_scope = d.pop("decision_scope")

        impact_digest = d.pop("impact_digest")

        interpretation_kind = d.pop("interpretation_kind")

        original_actionable_count = d.pop("original_actionable_count")

        parser_version = d.pop("parser_version")

        resolution_kind = d.pop("resolution_kind")

        resulting_actionable_count = d.pop("resulting_actionable_count")

        unit_registry_version = d.pop("unit_registry_version")

        convention = d.pop("convention", UNSET)

        def _parse_convention_unit_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                convention_unit_ids_type_0 = cast(list[str], data)

                return convention_unit_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        convention_unit_ids = _parse_convention_unit_ids(d.pop("convention_unit_ids", UNSET))


        def _parse_excluded_item_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_item_ids_type_0 = cast(list[str], data)

                return excluded_item_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        excluded_item_ids = _parse_excluded_item_ids(d.pop("excluded_item_ids", UNSET))


        def _parse_excluded_occurrence_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_occurrence_ids_type_0 = cast(list[str], data)

                return excluded_occurrence_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        excluded_occurrence_ids = _parse_excluded_occurrence_ids(d.pop("excluded_occurrence_ids", UNSET))


        def _parse_scope_ingredient_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scope_ingredient_ids_type_0 = cast(list[str], data)

                return scope_ingredient_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scope_ingredient_ids = _parse_scope_ingredient_ids(d.pop("scope_ingredient_ids", UNSET))


        def _parse_scope_occurrence_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scope_occurrence_keys_type_0 = cast(list[str], data)

                return scope_occurrence_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scope_occurrence_keys = _parse_scope_occurrence_keys(d.pop("scope_occurrence_keys", UNSET))


        unit_id = d.pop("unit_id", UNSET)

        import_resolution_decision = cls(
            affected_ingredient_count=affected_ingredient_count,
            affected_occurrence_ids=affected_occurrence_ids,
            affected_recipe_count=affected_recipe_count,
            decision_scope=decision_scope,
            impact_digest=impact_digest,
            interpretation_kind=interpretation_kind,
            original_actionable_count=original_actionable_count,
            parser_version=parser_version,
            resolution_kind=resolution_kind,
            resulting_actionable_count=resulting_actionable_count,
            unit_registry_version=unit_registry_version,
            convention=convention,
            convention_unit_ids=convention_unit_ids,
            excluded_item_ids=excluded_item_ids,
            excluded_occurrence_ids=excluded_occurrence_ids,
            scope_ingredient_ids=scope_ingredient_ids,
            scope_occurrence_keys=scope_occurrence_keys,
            unit_id=unit_id,
        )


        import_resolution_decision.additional_properties = d
        return import_resolution_decision

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
