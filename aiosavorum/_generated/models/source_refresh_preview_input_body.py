from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.recipe_document import RecipeDocument





T = TypeVar("T", bound="SourceRefreshPreviewInputBody")



@_attrs_define
class SourceRefreshPreviewInputBody:
    """ 
        Attributes:
            expected_revision (int):
            remote (RecipeDocument):
     """

    expected_revision: int
    remote: RecipeDocument





    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        expected_revision = self.expected_revision

        remote = self.remote.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expected_revision": expected_revision,
            "remote": remote,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        d = dict(src_dict)
        expected_revision = d.pop("expected_revision")

        remote = RecipeDocument.from_dict(d.pop("remote"))




        source_refresh_preview_input_body = cls(
            expected_revision=expected_revision,
            remote=remote,
        )

        return source_refresh_preview_input_body

