from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.facet_kind import FacetKind
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Facet")



@_attrs_define
class Facet:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (str):
            kind (FacetKind):
            revision (int):
            updated_at (datetime.datetime):
            value (str):
            recipe_count (int | Unset):
     """

    created_at: datetime.datetime
    id: str
    kind: FacetKind
    revision: int
    updated_at: datetime.datetime
    value: str
    recipe_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        kind = self.kind.value

        revision = self.revision

        updated_at = self.updated_at.isoformat()

        value = self.value

        recipe_count = self.recipe_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "kind": kind,
            "revision": revision,
            "updated_at": updated_at,
            "value": value,
        })
        if recipe_count is not UNSET:
            field_dict["recipe_count"] = recipe_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        kind = FacetKind(d.pop("kind"))




        revision = d.pop("revision")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        value = d.pop("value")

        recipe_count = d.pop("recipe_count", UNSET)

        facet = cls(
            created_at=created_at,
            id=id,
            kind=kind,
            revision=revision,
            updated_at=updated_at,
            value=value,
            recipe_count=recipe_count,
        )


        facet.additional_properties = d
        return facet

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
