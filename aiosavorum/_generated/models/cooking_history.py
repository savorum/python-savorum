from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.cooking_record import CookingRecord
  from ..models.imported_cook_count_baseline import ImportedCookCountBaseline





T = TypeVar("T", bound="CookingHistory")



@_attrs_define
class CookingHistory:
    """ 
        Attributes:
            items (list[CookingRecord] | None):
            library_entry_id (str):
            times_cooked (int):
            imported_baselines (list[ImportedCookCountBaseline] | None | Unset):
            last_cooked (datetime.date | Unset):
     """

    items: list[CookingRecord] | None
    library_entry_id: str
    times_cooked: int
    imported_baselines: list[ImportedCookCountBaseline] | None | Unset = UNSET
    last_cooked: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cooking_record import CookingRecord # noqa: PLC0415
        from ..models.imported_cook_count_baseline import ImportedCookCountBaseline # noqa: PLC0415
        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        library_entry_id = self.library_entry_id

        times_cooked = self.times_cooked

        imported_baselines: list[dict[str, Any]] | None | Unset
        if isinstance(self.imported_baselines, Unset):
            imported_baselines = UNSET
        elif isinstance(self.imported_baselines, list):
            imported_baselines = []
            for imported_baselines_type_0_item_data in self.imported_baselines:
                imported_baselines_type_0_item = imported_baselines_type_0_item_data.to_dict()
                imported_baselines.append(imported_baselines_type_0_item)


        else:
            imported_baselines = self.imported_baselines

        last_cooked: str | Unset = UNSET
        if not isinstance(self.last_cooked, Unset):
            last_cooked = self.last_cooked.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "items": items,
            "library_entry_id": library_entry_id,
            "times_cooked": times_cooked,
        })
        if imported_baselines is not UNSET:
            field_dict["imported_baselines"] = imported_baselines
        if last_cooked is not UNSET:
            field_dict["last_cooked"] = last_cooked

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cooking_record import CookingRecord # noqa: PLC0415
        from ..models.imported_cook_count_baseline import ImportedCookCountBaseline # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[CookingRecord] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = CookingRecord.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CookingRecord] | None, data)

        items = _parse_items(d.pop("items"))


        library_entry_id = d.pop("library_entry_id")

        times_cooked = d.pop("times_cooked")

        def _parse_imported_baselines(data: object) -> list[ImportedCookCountBaseline] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                imported_baselines_type_0 = []
                _imported_baselines_type_0 = data
                for imported_baselines_type_0_item_data in (_imported_baselines_type_0):
                    imported_baselines_type_0_item = ImportedCookCountBaseline.from_dict(imported_baselines_type_0_item_data)



                    imported_baselines_type_0.append(imported_baselines_type_0_item)

                return imported_baselines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportedCookCountBaseline] | None | Unset, data)

        imported_baselines = _parse_imported_baselines(d.pop("imported_baselines", UNSET))


        _last_cooked = d.pop("last_cooked", UNSET)
        last_cooked: datetime.date | Unset
        if isinstance(_last_cooked,  Unset):
            last_cooked = UNSET
        else:
            last_cooked = datetime.date.fromisoformat(_last_cooked)




        cooking_history = cls(
            items=items,
            library_entry_id=library_entry_id,
            times_cooked=times_cooked,
            imported_baselines=imported_baselines,
            last_cooked=last_cooked,
        )


        cooking_history.additional_properties = d
        return cooking_history

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
