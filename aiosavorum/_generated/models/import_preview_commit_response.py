from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_preview_response import ImportPreviewResponse
  from ..models.imported_recipe import ImportedRecipe





T = TypeVar("T", bound="ImportPreviewCommitResponse")



@_attrs_define
class ImportPreviewCommitResponse:
    """ 
        Attributes:
            items (list[ImportedRecipe] | None):
            remaining (ImportPreviewResponse | Unset):
     """

    items: list[ImportedRecipe] | None
    remaining: ImportPreviewResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_preview_response import ImportPreviewResponse # noqa: PLC0415
        from ..models.imported_recipe import ImportedRecipe # noqa: PLC0415
        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        remaining: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remaining, Unset):
            remaining = self.remaining.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "items": items,
        })
        if remaining is not UNSET:
            field_dict["remaining"] = remaining

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_preview_response import ImportPreviewResponse # noqa: PLC0415
        from ..models.imported_recipe import ImportedRecipe # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[ImportedRecipe] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = ImportedRecipe.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportedRecipe] | None, data)

        items = _parse_items(d.pop("items"))


        _remaining = d.pop("remaining", UNSET)
        remaining: ImportPreviewResponse | Unset
        if isinstance(_remaining,  Unset):
            remaining = UNSET
        else:
            remaining = ImportPreviewResponse.from_dict(_remaining)




        import_preview_commit_response = cls(
            items=items,
            remaining=remaining,
        )


        import_preview_commit_response.additional_properties = d
        return import_preview_commit_response

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
