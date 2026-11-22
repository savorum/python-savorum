from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="MeasurementResolutionOccurrence")



@_attrs_define
class MeasurementResolutionOccurrence:
    """ 
        Attributes:
            authored_form (str):
            candidate_unit_ids (list[str] | None):
            fingerprint (str):
            group_id (str):
            id (str):
            ingredient_id (str):
            item_id (str):
            recipe_id (str):
            recipe_title (str):
            resolution_key (str):
            source_text (str):
     """

    authored_form: str
    candidate_unit_ids: list[str] | None
    fingerprint: str
    group_id: str
    id: str
    ingredient_id: str
    item_id: str
    recipe_id: str
    recipe_title: str
    resolution_key: str
    source_text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        authored_form = self.authored_form

        candidate_unit_ids: list[str] | None
        if isinstance(self.candidate_unit_ids, list):
            candidate_unit_ids = self.candidate_unit_ids


        else:
            candidate_unit_ids = self.candidate_unit_ids

        fingerprint = self.fingerprint

        group_id = self.group_id

        id = self.id

        ingredient_id = self.ingredient_id

        item_id = self.item_id

        recipe_id = self.recipe_id

        recipe_title = self.recipe_title

        resolution_key = self.resolution_key

        source_text = self.source_text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "authored_form": authored_form,
            "candidate_unit_ids": candidate_unit_ids,
            "fingerprint": fingerprint,
            "group_id": group_id,
            "id": id,
            "ingredient_id": ingredient_id,
            "item_id": item_id,
            "recipe_id": recipe_id,
            "recipe_title": recipe_title,
            "resolution_key": resolution_key,
            "source_text": source_text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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


        fingerprint = d.pop("fingerprint")

        group_id = d.pop("group_id")

        id = d.pop("id")

        ingredient_id = d.pop("ingredient_id")

        item_id = d.pop("item_id")

        recipe_id = d.pop("recipe_id")

        recipe_title = d.pop("recipe_title")

        resolution_key = d.pop("resolution_key")

        source_text = d.pop("source_text")

        measurement_resolution_occurrence = cls(
            authored_form=authored_form,
            candidate_unit_ids=candidate_unit_ids,
            fingerprint=fingerprint,
            group_id=group_id,
            id=id,
            ingredient_id=ingredient_id,
            item_id=item_id,
            recipe_id=recipe_id,
            recipe_title=recipe_title,
            resolution_key=resolution_key,
            source_text=source_text,
        )


        measurement_resolution_occurrence.additional_properties = d
        return measurement_resolution_occurrence

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
