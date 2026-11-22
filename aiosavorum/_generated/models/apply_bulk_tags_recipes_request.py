from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.target import Target





T = TypeVar("T", bound="ApplyBulkTagsRecipesRequest")



@_attrs_define
class ApplyBulkTagsRecipesRequest:
    """ 
        Attributes:
            items (list[Target] | None):
            add_tags (list[str] | None | Unset):
            book_id (str | Unset):
            book_revision (int | Unset):
            member (bool | Unset):
            remove_tags (list[str] | None | Unset):
     """

    items: list[Target] | None
    add_tags: list[str] | None | Unset = UNSET
    book_id: str | Unset = UNSET
    book_revision: int | Unset = UNSET
    member: bool | Unset = UNSET
    remove_tags: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.target import Target # noqa: PLC0415
        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        add_tags: list[str] | None | Unset
        if isinstance(self.add_tags, Unset):
            add_tags = UNSET
        elif isinstance(self.add_tags, list):
            add_tags = self.add_tags


        else:
            add_tags = self.add_tags

        book_id = self.book_id

        book_revision = self.book_revision

        member = self.member

        remove_tags: list[str] | None | Unset
        if isinstance(self.remove_tags, Unset):
            remove_tags = UNSET
        elif isinstance(self.remove_tags, list):
            remove_tags = self.remove_tags


        else:
            remove_tags = self.remove_tags


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "items": items,
        })
        if add_tags is not UNSET:
            field_dict["add_tags"] = add_tags
        if book_id is not UNSET:
            field_dict["book_id"] = book_id
        if book_revision is not UNSET:
            field_dict["book_revision"] = book_revision
        if member is not UNSET:
            field_dict["member"] = member
        if remove_tags is not UNSET:
            field_dict["remove_tags"] = remove_tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target import Target # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[Target] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = Target.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Target] | None, data)

        items = _parse_items(d.pop("items"))


        def _parse_add_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                add_tags_type_0 = cast(list[str], data)

                return add_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        add_tags = _parse_add_tags(d.pop("add_tags", UNSET))


        book_id = d.pop("book_id", UNSET)

        book_revision = d.pop("book_revision", UNSET)

        member = d.pop("member", UNSET)

        def _parse_remove_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                remove_tags_type_0 = cast(list[str], data)

                return remove_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        remove_tags = _parse_remove_tags(d.pop("remove_tags", UNSET))


        apply_bulk_tags_recipes_request = cls(
            items=items,
            add_tags=add_tags,
            book_id=book_id,
            book_revision=book_revision,
            member=member,
            remove_tags=remove_tags,
        )

        return apply_bulk_tags_recipes_request

