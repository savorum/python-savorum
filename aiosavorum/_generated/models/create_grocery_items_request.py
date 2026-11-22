from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.addition import Addition





T = TypeVar("T", bound="CreateGroceryItemsRequest")



@_attrs_define
class CreateGroceryItemsRequest:
    """ 
        Attributes:
            items (list[Addition] | None):
     """

    items: list[Addition] | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.addition import Addition # noqa: PLC0415
        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "items": items,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.addition import Addition # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[Addition] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = Addition.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Addition] | None, data)

        items = _parse_items(d.pop("items"))


        create_grocery_items_request = cls(
            items=items,
        )

        return create_grocery_items_request

