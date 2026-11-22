from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.recipe_revision_summary_cause import RecipeRevisionSummaryCause
from ..models.recipe_revision_summary_changes_type_0_item import RecipeRevisionSummaryChangesType0Item
from ..models.recipe_revision_summary_state import RecipeRevisionSummaryState
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="RecipeRevisionSummary")



@_attrs_define
class RecipeRevisionSummary:
    """ 
        Attributes:
            cause (RecipeRevisionSummaryCause):
            created_at (datetime.datetime):
            library_entry_id (str):
            revision (int):
            state (RecipeRevisionSummaryState):
            actor_id (str | Unset):
            actor_name (str | Unset):
            changes (list[RecipeRevisionSummaryChangesType0Item] | None | Unset):
            source_revision (int | Unset):
     """

    cause: RecipeRevisionSummaryCause
    created_at: datetime.datetime
    library_entry_id: str
    revision: int
    state: RecipeRevisionSummaryState
    actor_id: str | Unset = UNSET
    actor_name: str | Unset = UNSET
    changes: list[RecipeRevisionSummaryChangesType0Item] | None | Unset = UNSET
    source_revision: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cause = self.cause.value

        created_at = self.created_at.isoformat()

        library_entry_id = self.library_entry_id

        revision = self.revision

        state = self.state.value

        actor_id = self.actor_id

        actor_name = self.actor_name

        changes: list[str] | None | Unset
        if isinstance(self.changes, Unset):
            changes = UNSET
        elif isinstance(self.changes, list):
            changes = []
            for changes_type_0_item_data in self.changes:
                changes_type_0_item = changes_type_0_item_data.value
                changes.append(changes_type_0_item)


        else:
            changes = self.changes

        source_revision = self.source_revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cause": cause,
            "created_at": created_at,
            "library_entry_id": library_entry_id,
            "revision": revision,
            "state": state,
        })
        if actor_id is not UNSET:
            field_dict["actor_id"] = actor_id
        if actor_name is not UNSET:
            field_dict["actor_name"] = actor_name
        if changes is not UNSET:
            field_dict["changes"] = changes
        if source_revision is not UNSET:
            field_dict["source_revision"] = source_revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cause = RecipeRevisionSummaryCause(d.pop("cause"))




        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        library_entry_id = d.pop("library_entry_id")

        revision = d.pop("revision")

        state = RecipeRevisionSummaryState(d.pop("state"))




        actor_id = d.pop("actor_id", UNSET)

        actor_name = d.pop("actor_name", UNSET)

        def _parse_changes(data: object) -> list[RecipeRevisionSummaryChangesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changes_type_0 = []
                _changes_type_0 = data
                for changes_type_0_item_data in (_changes_type_0):
                    changes_type_0_item = RecipeRevisionSummaryChangesType0Item(changes_type_0_item_data)



                    changes_type_0.append(changes_type_0_item)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RecipeRevisionSummaryChangesType0Item] | None | Unset, data)

        changes = _parse_changes(d.pop("changes", UNSET))


        source_revision = d.pop("source_revision", UNSET)

        recipe_revision_summary = cls(
            cause=cause,
            created_at=created_at,
            library_entry_id=library_entry_id,
            revision=revision,
            state=state,
            actor_id=actor_id,
            actor_name=actor_name,
            changes=changes,
            source_revision=source_revision,
        )


        recipe_revision_summary.additional_properties = d
        return recipe_revision_summary

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
