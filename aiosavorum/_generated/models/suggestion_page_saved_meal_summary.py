from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.saved_meal_summary import SavedMealSummary





T = TypeVar("T", bound="SuggestionPageSavedMealSummary")



@_attrs_define
class SuggestionPageSavedMealSummary:
    """ 
        Attributes:
            has_more (bool):
            items (list[SavedMealSummary] | None):
            limit (int):
            offset (int):
     """

    has_more: bool
    items: list[SavedMealSummary] | None
    limit: int
    offset: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.saved_meal_summary import SavedMealSummary # noqa: PLC0415
        has_more = self.has_more

        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        limit = self.limit

        offset = self.offset


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "has_more": has_more,
            "items": items,
            "limit": limit,
            "offset": offset,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saved_meal_summary import SavedMealSummary # noqa: PLC0415
        d = dict(src_dict)
        has_more = d.pop("has_more")

        def _parse_items(data: object) -> list[SavedMealSummary] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = SavedMealSummary.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SavedMealSummary] | None, data)

        items = _parse_items(d.pop("items"))


        limit = d.pop("limit")

        offset = d.pop("offset")

        suggestion_page_saved_meal_summary = cls(
            has_more=has_more,
            items=items,
            limit=limit,
            offset=offset,
        )


        suggestion_page_saved_meal_summary.additional_properties = d
        return suggestion_page_saved_meal_summary

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
