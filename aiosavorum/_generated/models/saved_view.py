from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.saved_view_sort import SavedViewSort
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="SavedView")



@_attrs_define
class SavedView:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (str):
            query (str):
            revision (int):
            title (str):
            updated_at (datetime.datetime):
            sort (SavedViewSort | Unset):
     """

    created_at: datetime.datetime
    id: str
    query: str
    revision: int
    title: str
    updated_at: datetime.datetime
    sort: SavedViewSort | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        query = self.query

        revision = self.revision

        title = self.title

        updated_at = self.updated_at.isoformat()

        sort: str | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "query": query,
            "revision": revision,
            "title": title,
            "updated_at": updated_at,
        })
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        query = d.pop("query")

        revision = d.pop("revision")

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        _sort = d.pop("sort", UNSET)
        sort: SavedViewSort | Unset
        if isinstance(_sort,  Unset):
            sort = UNSET
        else:
            sort = SavedViewSort(_sort)




        saved_view = cls(
            created_at=created_at,
            id=id,
            query=query,
            revision=revision,
            title=title,
            updated_at=updated_at,
            sort=sort,
        )


        saved_view.additional_properties = d
        return saved_view

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
