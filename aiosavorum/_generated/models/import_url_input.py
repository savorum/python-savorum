from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_url_input_on_duplicate import ImportURLInputOnDuplicate
from ..types import UNSET, Unset






T = TypeVar("T", bound="ImportURLInput")



@_attrs_define
class ImportURLInput:
    """ 
        Attributes:
            url (str):
            on_duplicate (ImportURLInputOnDuplicate | Unset):
     """

    url: str
    on_duplicate: ImportURLInputOnDuplicate | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        on_duplicate: str | Unset = UNSET
        if not isinstance(self.on_duplicate, Unset):
            on_duplicate = self.on_duplicate.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "url": url,
        })
        if on_duplicate is not UNSET:
            field_dict["on_duplicate"] = on_duplicate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        _on_duplicate = d.pop("on_duplicate", UNSET)
        on_duplicate: ImportURLInputOnDuplicate | Unset
        if isinstance(_on_duplicate,  Unset):
            on_duplicate = UNSET
        else:
            on_duplicate = ImportURLInputOnDuplicate(_on_duplicate)




        import_url_input = cls(
            url=url,
            on_duplicate=on_duplicate,
        )

        return import_url_input

