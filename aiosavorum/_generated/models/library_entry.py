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
  from ..models.recipe_document import RecipeDocument
  from ..models.time_summary import TimeSummary





T = TypeVar("T", bound="LibraryEntry")



@_attrs_define
class LibraryEntry:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (str): Identifier of this entry in the local Savorum library
            recipe (RecipeDocument):
            revision (int):
            time_summary (TimeSummary):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | Unset):
     """

    created_at: datetime.datetime
    id: str
    recipe: RecipeDocument
    revision: int
    time_summary: TimeSummary
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        from ..models.time_summary import TimeSummary # noqa: PLC0415
        created_at = self.created_at.isoformat()

        id = self.id

        recipe = self.recipe.to_dict()

        revision = self.revision

        time_summary = self.time_summary.to_dict()

        updated_at = self.updated_at.isoformat()

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "recipe": recipe,
            "revision": revision,
            "time_summary": time_summary,
            "updated_at": updated_at,
        })
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        from ..models.time_summary import TimeSummary # noqa: PLC0415
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        recipe = RecipeDocument.from_dict(d.pop("recipe"))




        revision = d.pop("revision")

        time_summary = TimeSummary.from_dict(d.pop("time_summary"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at,  Unset):
            deleted_at = UNSET
        else:
            deleted_at = datetime.datetime.fromisoformat(_deleted_at)




        library_entry = cls(
            created_at=created_at,
            id=id,
            recipe=recipe,
            revision=revision,
            time_summary=time_summary,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )


        library_entry.additional_properties = d
        return library_entry

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
