from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_preview_resolution_input_action import ImportPreviewResolutionInputAction
from ..types import UNSET, Unset






T = TypeVar("T", bound="ImportPreviewResolutionInput")



@_attrs_define
class ImportPreviewResolutionInput:
    """ 
        Attributes:
            action (ImportPreviewResolutionInputAction):
            item_id (str):
            target_entry_id (str | Unset):
     """

    action: ImportPreviewResolutionInputAction
    item_id: str
    target_entry_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        item_id = self.item_id

        target_entry_id = self.target_entry_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "action": action,
            "item_id": item_id,
        })
        if target_entry_id is not UNSET:
            field_dict["target_entry_id"] = target_entry_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = ImportPreviewResolutionInputAction(d.pop("action"))




        item_id = d.pop("item_id")

        target_entry_id = d.pop("target_entry_id", UNSET)

        import_preview_resolution_input = cls(
            action=action,
            item_id=item_id,
            target_entry_id=target_entry_id,
        )

        return import_preview_resolution_input

