from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.translation import Translation
  from ..models.translation_rendition import TranslationRendition





T = TypeVar("T", bound="RecipeTranslations")



@_attrs_define
class RecipeTranslations:
    """ 
        Attributes:
            renditions (list[TranslationRendition] | None): Other recipes in this library that are renditions of this one
            unresolved (list[Translation] | None): This recipe's own declarations that name no recipe in this library
            original (str | Unset): Library entry the renditions declare as their original, when they agree on one
     """

    renditions: list[TranslationRendition] | None
    unresolved: list[Translation] | None
    original: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.translation import Translation # noqa: PLC0415
        from ..models.translation_rendition import TranslationRendition # noqa: PLC0415
        renditions: list[dict[str, Any]] | None
        if isinstance(self.renditions, list):
            renditions = []
            for renditions_type_0_item_data in self.renditions:
                renditions_type_0_item = renditions_type_0_item_data.to_dict()
                renditions.append(renditions_type_0_item)


        else:
            renditions = self.renditions

        unresolved: list[dict[str, Any]] | None
        if isinstance(self.unresolved, list):
            unresolved = []
            for unresolved_type_0_item_data in self.unresolved:
                unresolved_type_0_item = unresolved_type_0_item_data.to_dict()
                unresolved.append(unresolved_type_0_item)


        else:
            unresolved = self.unresolved

        original = self.original


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "renditions": renditions,
            "unresolved": unresolved,
        })
        if original is not UNSET:
            field_dict["original"] = original

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.translation import Translation # noqa: PLC0415
        from ..models.translation_rendition import TranslationRendition # noqa: PLC0415
        d = dict(src_dict)
        def _parse_renditions(data: object) -> list[TranslationRendition] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                renditions_type_0 = []
                _renditions_type_0 = data
                for renditions_type_0_item_data in (_renditions_type_0):
                    renditions_type_0_item = TranslationRendition.from_dict(renditions_type_0_item_data)



                    renditions_type_0.append(renditions_type_0_item)

                return renditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TranslationRendition] | None, data)

        renditions = _parse_renditions(d.pop("renditions"))


        def _parse_unresolved(data: object) -> list[Translation] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unresolved_type_0 = []
                _unresolved_type_0 = data
                for unresolved_type_0_item_data in (_unresolved_type_0):
                    unresolved_type_0_item = Translation.from_dict(unresolved_type_0_item_data)



                    unresolved_type_0.append(unresolved_type_0_item)

                return unresolved_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Translation] | None, data)

        unresolved = _parse_unresolved(d.pop("unresolved"))


        original = d.pop("original", UNSET)

        recipe_translations = cls(
            renditions=renditions,
            unresolved=unresolved,
            original=original,
        )


        recipe_translations.additional_properties = d
        return recipe_translations

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
