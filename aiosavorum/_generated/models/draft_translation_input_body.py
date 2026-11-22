from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DraftTranslationInputBody")



@_attrs_define
class DraftTranslationInputBody:
    """ 
        Attributes:
            language (str): BCP 47 tag of the new rendition's language
            copy_content (bool | Unset): Start from a copy of this recipe's content, as ordinary editable text in its
                original language
            title (str | Unset):
     """

    language: str
    copy_content: bool | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        language = self.language

        copy_content = self.copy_content

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "language": language,
        })
        if copy_content is not UNSET:
            field_dict["copy_content"] = copy_content
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language")

        copy_content = d.pop("copy_content", UNSET)

        title = d.pop("title", UNSET)

        draft_translation_input_body = cls(
            language=language,
            copy_content=copy_content,
            title=title,
        )

        return draft_translation_input_body

