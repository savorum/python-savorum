from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.recipe_document import RecipeDocument





T = TypeVar("T", bound="MergeInputBody")



@_attrs_define
class MergeInputBody:
    """ 
        Attributes:
            duplicate (str):
            expected_duplicate_revision (int):
            expected_survivor_revision (int):
            recipe (RecipeDocument):
            survivor (str):
     """

    duplicate: str
    expected_duplicate_revision: int
    expected_survivor_revision: int
    recipe: RecipeDocument
    survivor: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        duplicate = self.duplicate

        expected_duplicate_revision = self.expected_duplicate_revision

        expected_survivor_revision = self.expected_survivor_revision

        recipe = self.recipe.to_dict()

        survivor = self.survivor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "duplicate": duplicate,
            "expected_duplicate_revision": expected_duplicate_revision,
            "expected_survivor_revision": expected_survivor_revision,
            "recipe": recipe,
            "survivor": survivor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        d = dict(src_dict)
        duplicate = d.pop("duplicate")

        expected_duplicate_revision = d.pop("expected_duplicate_revision")

        expected_survivor_revision = d.pop("expected_survivor_revision")

        recipe = RecipeDocument.from_dict(d.pop("recipe"))




        survivor = d.pop("survivor")

        merge_input_body = cls(
            duplicate=duplicate,
            expected_duplicate_revision=expected_duplicate_revision,
            expected_survivor_revision=expected_survivor_revision,
            recipe=recipe,
            survivor=survivor,
        )

        return merge_input_body

