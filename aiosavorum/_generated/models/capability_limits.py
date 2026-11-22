from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CapabilityLimits")



@_attrs_define
class CapabilityLimits:
    """ 
        Attributes:
            artifact_hours (int):
            async_items (int):
            bulk_items (int):
            export_artifact_bytes (int):
            export_recipes (int):
            grocery_addition_items (int):
            import_file_bytes (int):
            lookup_items (int):
            pantry_entries (int):
            request_body_bytes (int):
            retry_receipt_hours (int):
            suggestion_items (int):
            print_recipes (int | Unset): Most recipes one printed document holds, when printing is available
     """

    artifact_hours: int
    async_items: int
    bulk_items: int
    export_artifact_bytes: int
    export_recipes: int
    grocery_addition_items: int
    import_file_bytes: int
    lookup_items: int
    pantry_entries: int
    request_body_bytes: int
    retry_receipt_hours: int
    suggestion_items: int
    print_recipes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        artifact_hours = self.artifact_hours

        async_items = self.async_items

        bulk_items = self.bulk_items

        export_artifact_bytes = self.export_artifact_bytes

        export_recipes = self.export_recipes

        grocery_addition_items = self.grocery_addition_items

        import_file_bytes = self.import_file_bytes

        lookup_items = self.lookup_items

        pantry_entries = self.pantry_entries

        request_body_bytes = self.request_body_bytes

        retry_receipt_hours = self.retry_receipt_hours

        suggestion_items = self.suggestion_items

        print_recipes = self.print_recipes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "artifact_hours": artifact_hours,
            "async_items": async_items,
            "bulk_items": bulk_items,
            "export_artifact_bytes": export_artifact_bytes,
            "export_recipes": export_recipes,
            "grocery_addition_items": grocery_addition_items,
            "import_file_bytes": import_file_bytes,
            "lookup_items": lookup_items,
            "pantry_entries": pantry_entries,
            "request_body_bytes": request_body_bytes,
            "retry_receipt_hours": retry_receipt_hours,
            "suggestion_items": suggestion_items,
        })
        if print_recipes is not UNSET:
            field_dict["print_recipes"] = print_recipes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        artifact_hours = d.pop("artifact_hours")

        async_items = d.pop("async_items")

        bulk_items = d.pop("bulk_items")

        export_artifact_bytes = d.pop("export_artifact_bytes")

        export_recipes = d.pop("export_recipes")

        grocery_addition_items = d.pop("grocery_addition_items")

        import_file_bytes = d.pop("import_file_bytes")

        lookup_items = d.pop("lookup_items")

        pantry_entries = d.pop("pantry_entries")

        request_body_bytes = d.pop("request_body_bytes")

        retry_receipt_hours = d.pop("retry_receipt_hours")

        suggestion_items = d.pop("suggestion_items")

        print_recipes = d.pop("print_recipes", UNSET)

        capability_limits = cls(
            artifact_hours=artifact_hours,
            async_items=async_items,
            bulk_items=bulk_items,
            export_artifact_bytes=export_artifact_bytes,
            export_recipes=export_recipes,
            grocery_addition_items=grocery_addition_items,
            import_file_bytes=import_file_bytes,
            lookup_items=lookup_items,
            pantry_entries=pantry_entries,
            request_body_bytes=request_body_bytes,
            retry_receipt_hours=retry_receipt_hours,
            suggestion_items=suggestion_items,
            print_recipes=print_recipes,
        )


        capability_limits.additional_properties = d
        return capability_limits

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
