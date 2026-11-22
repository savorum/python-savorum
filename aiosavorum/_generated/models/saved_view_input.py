from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.saved_view_input_sort import SavedViewInputSort
from ..types import UNSET, Unset






T = TypeVar("T", bound="SavedViewInput")



@_attrs_define
class SavedViewInput:
    """ 
        Attributes:
            query (str):
            title (str):
            sort (SavedViewInputSort | Unset):
     """

    query: str
    title: str
    sort: SavedViewInputSort | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        query = self.query

        title = self.title

        sort: str | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "query": query,
            "title": title,
        })
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        title = d.pop("title")

        _sort = d.pop("sort", UNSET)
        sort: SavedViewInputSort | Unset
        if isinstance(_sort,  Unset):
            sort = UNSET
        else:
            sort = SavedViewInputSort(_sort)




        saved_view_input = cls(
            query=query,
            title=title,
            sort=sort,
        )

        return saved_view_input

