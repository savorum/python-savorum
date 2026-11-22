from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.recipe_summary import RecipeSummary





T = TypeVar("T", bound="LookupOutputRecipeSummaryBody")



@_attrs_define
class LookupOutputRecipeSummaryBody:
    """ 
        Attributes:
            items (list[RecipeSummary] | None):
            unresolved_ids (list[str] | None):
     """

    items: list[RecipeSummary] | None
    unresolved_ids: list[str] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_summary import RecipeSummary # noqa: PLC0415
        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        unresolved_ids: list[str] | None
        if isinstance(self.unresolved_ids, list):
            unresolved_ids = self.unresolved_ids


        else:
            unresolved_ids = self.unresolved_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "items": items,
            "unresolved_ids": unresolved_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_summary import RecipeSummary # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[RecipeSummary] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = RecipeSummary.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RecipeSummary] | None, data)

        items = _parse_items(d.pop("items"))


        def _parse_unresolved_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unresolved_ids_type_0 = cast(list[str], data)

                return unresolved_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        unresolved_ids = _parse_unresolved_ids(d.pop("unresolved_ids"))


        lookup_output_recipe_summary_body = cls(
            items=items,
            unresolved_ids=unresolved_ids,
        )


        lookup_output_recipe_summary_body.additional_properties = d
        return lookup_output_recipe_summary_body

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
