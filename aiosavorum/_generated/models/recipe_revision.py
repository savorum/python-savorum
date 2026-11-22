from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.recipe_revision_cause import RecipeRevisionCause
from ..models.recipe_revision_state import RecipeRevisionState
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.recipe_document import RecipeDocument





T = TypeVar("T", bound="RecipeRevision")



@_attrs_define
class RecipeRevision:
    """ 
        Attributes:
            cause (RecipeRevisionCause):
            created_at (datetime.datetime):
            library_entry_id (str): Identifier of the owning entry in the local Savorum library
            recipe (RecipeDocument):
            revision (int):
            state (RecipeRevisionState):
            actor_id (str | Unset):
            actor_name (str | Unset):
            source_revision (int | Unset):
     """

    cause: RecipeRevisionCause
    created_at: datetime.datetime
    library_entry_id: str
    recipe: RecipeDocument
    revision: int
    state: RecipeRevisionState
    actor_id: str | Unset = UNSET
    actor_name: str | Unset = UNSET
    source_revision: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        cause = self.cause.value

        created_at = self.created_at.isoformat()

        library_entry_id = self.library_entry_id

        recipe = self.recipe.to_dict()

        revision = self.revision

        state = self.state.value

        actor_id = self.actor_id

        actor_name = self.actor_name

        source_revision = self.source_revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cause": cause,
            "created_at": created_at,
            "library_entry_id": library_entry_id,
            "recipe": recipe,
            "revision": revision,
            "state": state,
        })
        if actor_id is not UNSET:
            field_dict["actor_id"] = actor_id
        if actor_name is not UNSET:
            field_dict["actor_name"] = actor_name
        if source_revision is not UNSET:
            field_dict["source_revision"] = source_revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        d = dict(src_dict)
        cause = RecipeRevisionCause(d.pop("cause"))




        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        library_entry_id = d.pop("library_entry_id")

        recipe = RecipeDocument.from_dict(d.pop("recipe"))




        revision = d.pop("revision")

        state = RecipeRevisionState(d.pop("state"))




        actor_id = d.pop("actor_id", UNSET)

        actor_name = d.pop("actor_name", UNSET)

        source_revision = d.pop("source_revision", UNSET)

        recipe_revision = cls(
            cause=cause,
            created_at=created_at,
            library_entry_id=library_entry_id,
            recipe=recipe,
            revision=revision,
            state=state,
            actor_id=actor_id,
            actor_name=actor_name,
            source_revision=source_revision,
        )


        recipe_revision.additional_properties = d
        return recipe_revision

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
