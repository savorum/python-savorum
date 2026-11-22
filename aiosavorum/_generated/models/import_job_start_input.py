from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_job_start_input_on_duplicate import ImportJobStartInputOnDuplicate
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_preview_resolution_input import ImportPreviewResolutionInput





T = TypeVar("T", bound="ImportJobStartInput")



@_attrs_define
class ImportJobStartInput:
    """ 
        Attributes:
            item_ids (list[str] | None | Unset):
            on_duplicate (ImportJobStartInputOnDuplicate | Unset):
            resolutions (list[ImportPreviewResolutionInput] | None | Unset):
            retain_source_item_ids (list[str] | None | Unset): Uploaded preview item IDs whose original files should be
                retained
     """

    item_ids: list[str] | None | Unset = UNSET
    on_duplicate: ImportJobStartInputOnDuplicate | Unset = UNSET
    resolutions: list[ImportPreviewResolutionInput] | None | Unset = UNSET
    retain_source_item_ids: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_preview_resolution_input import ImportPreviewResolutionInput # noqa: PLC0415
        item_ids: list[str] | None | Unset
        if isinstance(self.item_ids, Unset):
            item_ids = UNSET
        elif isinstance(self.item_ids, list):
            item_ids = self.item_ids


        else:
            item_ids = self.item_ids

        on_duplicate: str | Unset = UNSET
        if not isinstance(self.on_duplicate, Unset):
            on_duplicate = self.on_duplicate.value


        resolutions: list[dict[str, Any]] | None | Unset
        if isinstance(self.resolutions, Unset):
            resolutions = UNSET
        elif isinstance(self.resolutions, list):
            resolutions = []
            for resolutions_type_0_item_data in self.resolutions:
                resolutions_type_0_item = resolutions_type_0_item_data.to_dict()
                resolutions.append(resolutions_type_0_item)


        else:
            resolutions = self.resolutions

        retain_source_item_ids: list[str] | None | Unset
        if isinstance(self.retain_source_item_ids, Unset):
            retain_source_item_ids = UNSET
        elif isinstance(self.retain_source_item_ids, list):
            retain_source_item_ids = self.retain_source_item_ids


        else:
            retain_source_item_ids = self.retain_source_item_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if item_ids is not UNSET:
            field_dict["item_ids"] = item_ids
        if on_duplicate is not UNSET:
            field_dict["on_duplicate"] = on_duplicate
        if resolutions is not UNSET:
            field_dict["resolutions"] = resolutions
        if retain_source_item_ids is not UNSET:
            field_dict["retain_source_item_ids"] = retain_source_item_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_preview_resolution_input import ImportPreviewResolutionInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_item_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                item_ids_type_0 = cast(list[str], data)

                return item_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        item_ids = _parse_item_ids(d.pop("item_ids", UNSET))


        _on_duplicate = d.pop("on_duplicate", UNSET)
        on_duplicate: ImportJobStartInputOnDuplicate | Unset
        if isinstance(_on_duplicate,  Unset):
            on_duplicate = UNSET
        else:
            on_duplicate = ImportJobStartInputOnDuplicate(_on_duplicate)




        def _parse_resolutions(data: object) -> list[ImportPreviewResolutionInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolutions_type_0 = []
                _resolutions_type_0 = data
                for resolutions_type_0_item_data in (_resolutions_type_0):
                    resolutions_type_0_item = ImportPreviewResolutionInput.from_dict(resolutions_type_0_item_data)



                    resolutions_type_0.append(resolutions_type_0_item)

                return resolutions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportPreviewResolutionInput] | None | Unset, data)

        resolutions = _parse_resolutions(d.pop("resolutions", UNSET))


        def _parse_retain_source_item_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                retain_source_item_ids_type_0 = cast(list[str], data)

                return retain_source_item_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        retain_source_item_ids = _parse_retain_source_item_ids(d.pop("retain_source_item_ids", UNSET))


        import_job_start_input = cls(
            item_ids=item_ids,
            on_duplicate=on_duplicate,
            resolutions=resolutions,
            retain_source_item_ids=retain_source_item_ids,
        )

        return import_job_start_input

