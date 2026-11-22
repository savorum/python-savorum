from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.recipe_document import RecipeDocument
  from ..models.source_refresh_conflict_wire import SourceRefreshConflictWire





T = TypeVar("T", bound="SourceRefreshPreviewWire")



@_attrs_define
class SourceRefreshPreviewWire:
    """ 
        Attributes:
            base (RecipeDocument):
            base_revision (int):
            conflicts (list[SourceRefreshConflictWire] | None):
            entry_id (str):
            expected_revision (int):
            id (str):
            local (RecipeDocument):
            merged (RecipeDocument):
            remote (RecipeDocument):
            summary (list[str] | None):
     """

    base: RecipeDocument
    base_revision: int
    conflicts: list[SourceRefreshConflictWire] | None
    entry_id: str
    expected_revision: int
    id: str
    local: RecipeDocument
    merged: RecipeDocument
    remote: RecipeDocument
    summary: list[str] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        from ..models.source_refresh_conflict_wire import SourceRefreshConflictWire # noqa: PLC0415
        base = self.base.to_dict()

        base_revision = self.base_revision

        conflicts: list[dict[str, Any]] | None
        if isinstance(self.conflicts, list):
            conflicts = []
            for conflicts_type_0_item_data in self.conflicts:
                conflicts_type_0_item = conflicts_type_0_item_data.to_dict()
                conflicts.append(conflicts_type_0_item)


        else:
            conflicts = self.conflicts

        entry_id = self.entry_id

        expected_revision = self.expected_revision

        id = self.id

        local = self.local.to_dict()

        merged = self.merged.to_dict()

        remote = self.remote.to_dict()

        summary: list[str] | None
        if isinstance(self.summary, list):
            summary = self.summary


        else:
            summary = self.summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "base": base,
            "base_revision": base_revision,
            "conflicts": conflicts,
            "entry_id": entry_id,
            "expected_revision": expected_revision,
            "id": id,
            "local": local,
            "merged": merged,
            "remote": remote,
            "summary": summary,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        from ..models.source_refresh_conflict_wire import SourceRefreshConflictWire # noqa: PLC0415
        d = dict(src_dict)
        base = RecipeDocument.from_dict(d.pop("base"))




        base_revision = d.pop("base_revision")

        def _parse_conflicts(data: object) -> list[SourceRefreshConflictWire] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conflicts_type_0 = []
                _conflicts_type_0 = data
                for conflicts_type_0_item_data in (_conflicts_type_0):
                    conflicts_type_0_item = SourceRefreshConflictWire.from_dict(conflicts_type_0_item_data)



                    conflicts_type_0.append(conflicts_type_0_item)

                return conflicts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SourceRefreshConflictWire] | None, data)

        conflicts = _parse_conflicts(d.pop("conflicts"))


        entry_id = d.pop("entry_id")

        expected_revision = d.pop("expected_revision")

        id = d.pop("id")

        local = RecipeDocument.from_dict(d.pop("local"))




        merged = RecipeDocument.from_dict(d.pop("merged"))




        remote = RecipeDocument.from_dict(d.pop("remote"))




        def _parse_summary(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                summary_type_0 = cast(list[str], data)

                return summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        summary = _parse_summary(d.pop("summary"))


        source_refresh_preview_wire = cls(
            base=base,
            base_revision=base_revision,
            conflicts=conflicts,
            entry_id=entry_id,
            expected_revision=expected_revision,
            id=id,
            local=local,
            merged=merged,
            remote=remote,
            summary=summary,
        )


        source_refresh_preview_wire.additional_properties = d
        return source_refresh_preview_wire

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
