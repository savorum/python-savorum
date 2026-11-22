from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_item_result import BulkItemResult





T = TypeVar("T", bound="JobResultsOutputBody")



@_attrs_define
class JobResultsOutputBody:
    """ 
        Attributes:
            items (list[BulkItemResult] | None):
            next_offset (int):
            total (int):
     """

    items: list[BulkItemResult] | None
    next_offset: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_item_result import BulkItemResult # noqa: PLC0415
        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        next_offset = self.next_offset

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "items": items,
            "next_offset": next_offset,
            "total": total,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_item_result import BulkItemResult # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[BulkItemResult] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = BulkItemResult.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BulkItemResult] | None, data)

        items = _parse_items(d.pop("items"))


        next_offset = d.pop("next_offset")

        total = d.pop("total")

        job_results_output_body = cls(
            items=items,
            next_offset=next_offset,
            total=total,
        )


        job_results_output_body.additional_properties = d
        return job_results_output_body

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
