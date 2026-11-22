from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.shopping_change_kind import ShoppingChangeKind
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ShoppingChange")



@_attrs_define
class ShoppingChange:
    """ 
        Attributes:
            base_revision (int):
            id (str):
            item_id (str):
            kind (ShoppingChangeKind):
            after_item_id (str | Unset):
            bought (bool | Unset):
            buy (str | Unset):
            category (str | Unset):
            merge_item_ids (list[str] | None | Unset):
            name (str | Unset):
            note (str | Unset):
            source_ids (list[str] | None | Unset):
     """

    base_revision: int
    id: str
    item_id: str
    kind: ShoppingChangeKind
    after_item_id: str | Unset = UNSET
    bought: bool | Unset = UNSET
    buy: str | Unset = UNSET
    category: str | Unset = UNSET
    merge_item_ids: list[str] | None | Unset = UNSET
    name: str | Unset = UNSET
    note: str | Unset = UNSET
    source_ids: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        base_revision = self.base_revision

        id = self.id

        item_id = self.item_id

        kind = self.kind.value

        after_item_id = self.after_item_id

        bought = self.bought

        buy = self.buy

        category = self.category

        merge_item_ids: list[str] | None | Unset
        if isinstance(self.merge_item_ids, Unset):
            merge_item_ids = UNSET
        elif isinstance(self.merge_item_ids, list):
            merge_item_ids = self.merge_item_ids


        else:
            merge_item_ids = self.merge_item_ids

        name = self.name

        note = self.note

        source_ids: list[str] | None | Unset
        if isinstance(self.source_ids, Unset):
            source_ids = UNSET
        elif isinstance(self.source_ids, list):
            source_ids = self.source_ids


        else:
            source_ids = self.source_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "base_revision": base_revision,
            "id": id,
            "item_id": item_id,
            "kind": kind,
        })
        if after_item_id is not UNSET:
            field_dict["after_item_id"] = after_item_id
        if bought is not UNSET:
            field_dict["bought"] = bought
        if buy is not UNSET:
            field_dict["buy"] = buy
        if category is not UNSET:
            field_dict["category"] = category
        if merge_item_ids is not UNSET:
            field_dict["merge_item_ids"] = merge_item_ids
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if source_ids is not UNSET:
            field_dict["source_ids"] = source_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_revision = d.pop("base_revision")

        id = d.pop("id")

        item_id = d.pop("item_id")

        kind = ShoppingChangeKind(d.pop("kind"))




        after_item_id = d.pop("after_item_id", UNSET)

        bought = d.pop("bought", UNSET)

        buy = d.pop("buy", UNSET)

        category = d.pop("category", UNSET)

        def _parse_merge_item_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                merge_item_ids_type_0 = cast(list[str], data)

                return merge_item_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        merge_item_ids = _parse_merge_item_ids(d.pop("merge_item_ids", UNSET))


        name = d.pop("name", UNSET)

        note = d.pop("note", UNSET)

        def _parse_source_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_ids_type_0 = cast(list[str], data)

                return source_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        source_ids = _parse_source_ids(d.pop("source_ids", UNSET))


        shopping_change = cls(
            base_revision=base_revision,
            id=id,
            item_id=item_id,
            kind=kind,
            after_item_id=after_item_id,
            bought=bought,
            buy=buy,
            category=category,
            merge_item_ids=merge_item_ids,
            name=name,
            note=note,
            source_ids=source_ids,
        )

        return shopping_change

