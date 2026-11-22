from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="LookupInputBody")



@_attrs_define
class LookupInputBody:
    """ 
        Attributes:
            ids (list[str] | None):
     """

    ids: list[str] | None





    def to_dict(self) -> dict[str, Any]:
        ids: list[str] | None
        if isinstance(self.ids, list):
            ids = self.ids


        else:
            ids = self.ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ids": ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = cast(list[str], data)

                return ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        ids = _parse_ids(d.pop("ids"))


        lookup_input_body = cls(
            ids=ids,
        )

        return lookup_input_body

