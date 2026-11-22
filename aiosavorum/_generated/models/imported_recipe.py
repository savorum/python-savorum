from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.imported_recipe_outcome import ImportedRecipeOutcome
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ImportedRecipe")



@_attrs_define
class ImportedRecipe:
    """ 
        Attributes:
            deferred_assets (int): Images not fetched yet whose addresses the recipe retains
            dropped_assets (int): Images the recipe named that could not be retrieved and were left out
            library_entry_id (str):
            outcome (ImportedRecipeOutcome):
            recipe_id (str):
            revision (int):
            title (str):
            import_event_id (str | Unset):
            warnings (list[str] | None | Unset): What the import had to work around, in the reader's words
     """

    deferred_assets: int
    dropped_assets: int
    library_entry_id: str
    outcome: ImportedRecipeOutcome
    recipe_id: str
    revision: int
    title: str
    import_event_id: str | Unset = UNSET
    warnings: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        deferred_assets = self.deferred_assets

        dropped_assets = self.dropped_assets

        library_entry_id = self.library_entry_id

        outcome = self.outcome.value

        recipe_id = self.recipe_id

        revision = self.revision

        title = self.title

        import_event_id = self.import_event_id

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings


        else:
            warnings = self.warnings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "deferred_assets": deferred_assets,
            "dropped_assets": dropped_assets,
            "library_entry_id": library_entry_id,
            "outcome": outcome,
            "recipe_id": recipe_id,
            "revision": revision,
            "title": title,
        })
        if import_event_id is not UNSET:
            field_dict["import_event_id"] = import_event_id
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deferred_assets = d.pop("deferred_assets")

        dropped_assets = d.pop("dropped_assets")

        library_entry_id = d.pop("library_entry_id")

        outcome = ImportedRecipeOutcome(d.pop("outcome"))




        recipe_id = d.pop("recipe_id")

        revision = d.pop("revision")

        title = d.pop("title")

        import_event_id = d.pop("import_event_id", UNSET)

        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))


        imported_recipe = cls(
            deferred_assets=deferred_assets,
            dropped_assets=dropped_assets,
            library_entry_id=library_entry_id,
            outcome=outcome,
            recipe_id=recipe_id,
            revision=revision,
            title=title,
            import_event_id=import_event_id,
            warnings=warnings,
        )


        imported_recipe.additional_properties = d
        return imported_recipe

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
