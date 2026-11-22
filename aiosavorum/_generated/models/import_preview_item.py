from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_preview_analysis import ImportPreviewAnalysis
  from ..models.import_preview_assets import ImportPreviewAssets
  from ..models.import_preview_diagnostic import ImportPreviewDiagnostic
  from ..models.import_preview_recipe import ImportPreviewRecipe
  from ..models.import_preview_source import ImportPreviewSource
  from ..models.recipe_document import RecipeDocument





T = TypeVar("T", bound="ImportPreviewItem")



@_attrs_define
class ImportPreviewItem:
    """ 
        Attributes:
            already_here (bool):
            analysis (ImportPreviewAnalysis):
            assets (ImportPreviewAssets):
            can_commit (bool):
            diagnostics (list[ImportPreviewDiagnostic] | None):
            id (str):
            recipe (ImportPreviewRecipe):
            source (ImportPreviewSource):
            document (RecipeDocument | Unset):
     """

    already_here: bool
    analysis: ImportPreviewAnalysis
    assets: ImportPreviewAssets
    can_commit: bool
    diagnostics: list[ImportPreviewDiagnostic] | None
    id: str
    recipe: ImportPreviewRecipe
    source: ImportPreviewSource
    document: RecipeDocument | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_preview_analysis import ImportPreviewAnalysis # noqa: PLC0415
        from ..models.import_preview_assets import ImportPreviewAssets # noqa: PLC0415
        from ..models.import_preview_diagnostic import ImportPreviewDiagnostic # noqa: PLC0415
        from ..models.import_preview_recipe import ImportPreviewRecipe # noqa: PLC0415
        from ..models.import_preview_source import ImportPreviewSource # noqa: PLC0415
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        already_here = self.already_here

        analysis = self.analysis.to_dict()

        assets = self.assets.to_dict()

        can_commit = self.can_commit

        diagnostics: list[dict[str, Any]] | None
        if isinstance(self.diagnostics, list):
            diagnostics = []
            for diagnostics_type_0_item_data in self.diagnostics:
                diagnostics_type_0_item = diagnostics_type_0_item_data.to_dict()
                diagnostics.append(diagnostics_type_0_item)


        else:
            diagnostics = self.diagnostics

        id = self.id

        recipe = self.recipe.to_dict()

        source = self.source.to_dict()

        document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "already_here": already_here,
            "analysis": analysis,
            "assets": assets,
            "can_commit": can_commit,
            "diagnostics": diagnostics,
            "id": id,
            "recipe": recipe,
            "source": source,
        })
        if document is not UNSET:
            field_dict["document"] = document

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_preview_analysis import ImportPreviewAnalysis # noqa: PLC0415
        from ..models.import_preview_assets import ImportPreviewAssets # noqa: PLC0415
        from ..models.import_preview_diagnostic import ImportPreviewDiagnostic # noqa: PLC0415
        from ..models.import_preview_recipe import ImportPreviewRecipe # noqa: PLC0415
        from ..models.import_preview_source import ImportPreviewSource # noqa: PLC0415
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        d = dict(src_dict)
        already_here = d.pop("already_here")

        analysis = ImportPreviewAnalysis.from_dict(d.pop("analysis"))




        assets = ImportPreviewAssets.from_dict(d.pop("assets"))




        can_commit = d.pop("can_commit")

        def _parse_diagnostics(data: object) -> list[ImportPreviewDiagnostic] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                diagnostics_type_0 = []
                _diagnostics_type_0 = data
                for diagnostics_type_0_item_data in (_diagnostics_type_0):
                    diagnostics_type_0_item = ImportPreviewDiagnostic.from_dict(diagnostics_type_0_item_data)



                    diagnostics_type_0.append(diagnostics_type_0_item)

                return diagnostics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportPreviewDiagnostic] | None, data)

        diagnostics = _parse_diagnostics(d.pop("diagnostics"))


        id = d.pop("id")

        recipe = ImportPreviewRecipe.from_dict(d.pop("recipe"))




        source = ImportPreviewSource.from_dict(d.pop("source"))




        _document = d.pop("document", UNSET)
        document: RecipeDocument | Unset
        if isinstance(_document,  Unset):
            document = UNSET
        else:
            document = RecipeDocument.from_dict(_document)




        import_preview_item = cls(
            already_here=already_here,
            analysis=analysis,
            assets=assets,
            can_commit=can_commit,
            diagnostics=diagnostics,
            id=id,
            recipe=recipe,
            source=source,
            document=document,
        )


        import_preview_item.additional_properties = d
        return import_preview_item

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
