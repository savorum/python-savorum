from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.print_format import PrintFormat
  from ..models.printed_recipe import PrintedRecipe





T = TypeVar("T", bound="PrintDocumentInfo")



@_attrs_define
class PrintDocumentInfo:
    """ 
        Attributes:
            bytes_ (int):
            filename (str): Suggested filename for a download
            format_ (PrintFormat):
            id (str): Signature of the renderer, effective title, source identity and revision, authorization scope, recipe
                revisions, preferences, and print options
            pages (int):
            recipes (list[PrintedRecipe] | None): Exactly which version of each recipe was printed
            title (str):
            url (str): Where to read the generated PDF
            warnings (list[str] | None | Unset): What degraded without invalidating the document, such as a photograph this
                library no longer holds
     """

    bytes_: int
    filename: str
    format_: PrintFormat
    id: str
    pages: int
    recipes: list[PrintedRecipe] | None
    title: str
    url: str
    warnings: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.print_format import PrintFormat # noqa: PLC0415
        from ..models.printed_recipe import PrintedRecipe # noqa: PLC0415
        bytes_ = self.bytes_

        filename = self.filename

        format_ = self.format_.to_dict()

        id = self.id

        pages = self.pages

        recipes: list[dict[str, Any]] | None
        if isinstance(self.recipes, list):
            recipes = []
            for recipes_type_0_item_data in self.recipes:
                recipes_type_0_item = recipes_type_0_item_data.to_dict()
                recipes.append(recipes_type_0_item)


        else:
            recipes = self.recipes

        title = self.title

        url = self.url

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
            "bytes": bytes_,
            "filename": filename,
            "format": format_,
            "id": id,
            "pages": pages,
            "recipes": recipes,
            "title": title,
            "url": url,
        })
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.print_format import PrintFormat # noqa: PLC0415
        from ..models.printed_recipe import PrintedRecipe # noqa: PLC0415
        d = dict(src_dict)
        bytes_ = d.pop("bytes")

        filename = d.pop("filename")

        format_ = PrintFormat.from_dict(d.pop("format"))




        id = d.pop("id")

        pages = d.pop("pages")

        def _parse_recipes(data: object) -> list[PrintedRecipe] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recipes_type_0 = []
                _recipes_type_0 = data
                for recipes_type_0_item_data in (_recipes_type_0):
                    recipes_type_0_item = PrintedRecipe.from_dict(recipes_type_0_item_data)



                    recipes_type_0.append(recipes_type_0_item)

                return recipes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrintedRecipe] | None, data)

        recipes = _parse_recipes(d.pop("recipes"))


        title = d.pop("title")

        url = d.pop("url")

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


        print_document_info = cls(
            bytes_=bytes_,
            filename=filename,
            format_=format_,
            id=id,
            pages=pages,
            recipes=recipes,
            title=title,
            url=url,
            warnings=warnings,
        )


        print_document_info.additional_properties = d
        return print_document_info

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
