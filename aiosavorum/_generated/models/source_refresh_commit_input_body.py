from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.recipe_document import RecipeDocument
  from ..models.refresh_resolution import RefreshResolution





T = TypeVar("T", bound="SourceRefreshCommitInputBody")



@_attrs_define
class SourceRefreshCommitInputBody:
    """ 
        Attributes:
            expected_revision (int):
            remote (RecipeDocument):
            resolutions (list[RefreshResolution] | None | Unset):
     """

    expected_revision: int
    remote: RecipeDocument
    resolutions: list[RefreshResolution] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        from ..models.refresh_resolution import RefreshResolution # noqa: PLC0415
        expected_revision = self.expected_revision

        remote = self.remote.to_dict()

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expected_revision": expected_revision,
            "remote": remote,
        })
        if resolutions is not UNSET:
            field_dict["resolutions"] = resolutions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        from ..models.refresh_resolution import RefreshResolution # noqa: PLC0415
        d = dict(src_dict)
        expected_revision = d.pop("expected_revision")

        remote = RecipeDocument.from_dict(d.pop("remote"))




        def _parse_resolutions(data: object) -> list[RefreshResolution] | None | Unset:
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
                    resolutions_type_0_item = RefreshResolution.from_dict(resolutions_type_0_item_data)



                    resolutions_type_0.append(resolutions_type_0_item)

                return resolutions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RefreshResolution] | None | Unset, data)

        resolutions = _parse_resolutions(d.pop("resolutions", UNSET))


        source_refresh_commit_input_body = cls(
            expected_revision=expected_revision,
            remote=remote,
            resolutions=resolutions,
        )

        return source_refresh_commit_input_body

