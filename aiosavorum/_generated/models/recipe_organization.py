from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.recipe_source import RecipeSource
  from ..models.user_state import UserState





T = TypeVar("T", bound="RecipeOrganization")



@_attrs_define
class RecipeOrganization:
    """ 
        Attributes:
            facet_ids (list[str] | None):
            library_entry_id (str): Identifier of the organized entry in the local Savorum library
            revision (int):
            sources (list[RecipeSource] | None):
            tag_ids (list[str] | None):
            updated_at (datetime.datetime):
            user_state (UserState):
     """

    facet_ids: list[str] | None
    library_entry_id: str
    revision: int
    sources: list[RecipeSource] | None
    tag_ids: list[str] | None
    updated_at: datetime.datetime
    user_state: UserState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_source import RecipeSource # noqa: PLC0415
        from ..models.user_state import UserState # noqa: PLC0415
        facet_ids: list[str] | None
        if isinstance(self.facet_ids, list):
            facet_ids = self.facet_ids


        else:
            facet_ids = self.facet_ids

        library_entry_id = self.library_entry_id

        revision = self.revision

        sources: list[dict[str, Any]] | None
        if isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)


        else:
            sources = self.sources

        tag_ids: list[str] | None
        if isinstance(self.tag_ids, list):
            tag_ids = self.tag_ids


        else:
            tag_ids = self.tag_ids

        updated_at = self.updated_at.isoformat()

        user_state = self.user_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "facet_ids": facet_ids,
            "library_entry_id": library_entry_id,
            "revision": revision,
            "sources": sources,
            "tag_ids": tag_ids,
            "updated_at": updated_at,
            "user_state": user_state,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_source import RecipeSource # noqa: PLC0415
        from ..models.user_state import UserState # noqa: PLC0415
        d = dict(src_dict)
        def _parse_facet_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facet_ids_type_0 = cast(list[str], data)

                return facet_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        facet_ids = _parse_facet_ids(d.pop("facet_ids"))


        library_entry_id = d.pop("library_entry_id")

        revision = d.pop("revision")

        def _parse_sources(data: object) -> list[RecipeSource] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in (_sources_type_0):
                    sources_type_0_item = RecipeSource.from_dict(sources_type_0_item_data)



                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RecipeSource] | None, data)

        sources = _parse_sources(d.pop("sources"))


        def _parse_tag_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tag_ids_type_0 = cast(list[str], data)

                return tag_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tag_ids = _parse_tag_ids(d.pop("tag_ids"))


        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        user_state = UserState.from_dict(d.pop("user_state"))




        recipe_organization = cls(
            facet_ids=facet_ids,
            library_entry_id=library_entry_id,
            revision=revision,
            sources=sources,
            tag_ids=tag_ids,
            updated_at=updated_at,
            user_state=user_state,
        )


        recipe_organization.additional_properties = d
        return recipe_organization

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
