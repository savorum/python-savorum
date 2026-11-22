from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.preference_values import PreferenceValues





T = TypeVar("T", bound="PreferencesInputBody")



@_attrs_define
class PreferencesInputBody:
    """ 
        Attributes:
            overrides (PreferenceValues):
            revision (int):
     """

    overrides: PreferenceValues
    revision: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.preference_values import PreferenceValues # noqa: PLC0415
        overrides = self.overrides.to_dict()

        revision = self.revision


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "overrides": overrides,
            "revision": revision,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preference_values import PreferenceValues # noqa: PLC0415
        d = dict(src_dict)
        overrides = PreferenceValues.from_dict(d.pop("overrides"))




        revision = d.pop("revision")

        preferences_input_body = cls(
            overrides=overrides,
            revision=revision,
        )

        return preferences_input_body

