from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.library_entry import LibraryEntry
  from ..models.merge_conflict_wire import MergeConflictWire
  from ..models.recipe_document import RecipeDocument





T = TypeVar("T", bound="MergePreviewWire")



@_attrs_define
class MergePreviewWire:
    """ 
        Attributes:
            conflicts (list[MergeConflictWire] | None):
            left (LibraryEntry):
            right (LibraryEntry):
            suggested (RecipeDocument):
     """

    conflicts: list[MergeConflictWire] | None
    left: LibraryEntry
    right: LibraryEntry
    suggested: RecipeDocument
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.library_entry import LibraryEntry # noqa: PLC0415
        from ..models.merge_conflict_wire import MergeConflictWire # noqa: PLC0415
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        conflicts: list[dict[str, Any]] | None
        if isinstance(self.conflicts, list):
            conflicts = []
            for conflicts_type_0_item_data in self.conflicts:
                conflicts_type_0_item = conflicts_type_0_item_data.to_dict()
                conflicts.append(conflicts_type_0_item)


        else:
            conflicts = self.conflicts

        left = self.left.to_dict()

        right = self.right.to_dict()

        suggested = self.suggested.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "conflicts": conflicts,
            "left": left,
            "right": right,
            "suggested": suggested,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_entry import LibraryEntry # noqa: PLC0415
        from ..models.merge_conflict_wire import MergeConflictWire # noqa: PLC0415
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        d = dict(src_dict)
        def _parse_conflicts(data: object) -> list[MergeConflictWire] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conflicts_type_0 = []
                _conflicts_type_0 = data
                for conflicts_type_0_item_data in (_conflicts_type_0):
                    conflicts_type_0_item = MergeConflictWire.from_dict(conflicts_type_0_item_data)



                    conflicts_type_0.append(conflicts_type_0_item)

                return conflicts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MergeConflictWire] | None, data)

        conflicts = _parse_conflicts(d.pop("conflicts"))


        left = LibraryEntry.from_dict(d.pop("left"))




        right = LibraryEntry.from_dict(d.pop("right"))




        suggested = RecipeDocument.from_dict(d.pop("suggested"))




        merge_preview_wire = cls(
            conflicts=conflicts,
            left=left,
            right=right,
            suggested=suggested,
        )


        merge_preview_wire.additional_properties = d
        return merge_preview_wire

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
