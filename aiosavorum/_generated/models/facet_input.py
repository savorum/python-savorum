from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.facet_input_kind import FacetInputKind






T = TypeVar("T", bound="FacetInput")



@_attrs_define
class FacetInput:
    """ 
        Attributes:
            kind (FacetInputKind):
            value (str):
     """

    kind: FacetInputKind
    value: str





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = FacetInputKind(d.pop("kind"))




        value = d.pop("value")

        facet_input = cls(
            kind=kind,
            value=value,
        )

        return facet_input

