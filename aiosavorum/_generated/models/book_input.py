from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.book_input_kind import BookInputKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.book_entry_input import BookEntryInput
  from ..models.book_section import BookSection





T = TypeVar("T", bound="BookInput")



@_attrs_define
class BookInput:
    """ 
        Attributes:
            entries (list[BookEntryInput] | None):
            kind (BookInputKind):
            sections (list[BookSection] | None):
            title (str):
            author (str | Unset):
            cover_asset_id (str | Unset):
            description (str | Unset):
            edition (str | Unset):
            editor (str | Unset):
            isbn (str | Unset):
            publication_date (str | Unset):
            publisher (str | Unset):
            subtitle (str | Unset):
     """

    entries: list[BookEntryInput] | None
    kind: BookInputKind
    sections: list[BookSection] | None
    title: str
    author: str | Unset = UNSET
    cover_asset_id: str | Unset = UNSET
    description: str | Unset = UNSET
    edition: str | Unset = UNSET
    editor: str | Unset = UNSET
    isbn: str | Unset = UNSET
    publication_date: str | Unset = UNSET
    publisher: str | Unset = UNSET
    subtitle: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.book_entry_input import BookEntryInput # noqa: PLC0415
        from ..models.book_section import BookSection # noqa: PLC0415
        entries: list[dict[str, Any]] | None
        if isinstance(self.entries, list):
            entries = []
            for entries_type_0_item_data in self.entries:
                entries_type_0_item = entries_type_0_item_data.to_dict()
                entries.append(entries_type_0_item)


        else:
            entries = self.entries

        kind = self.kind.value

        sections: list[dict[str, Any]] | None
        if isinstance(self.sections, list):
            sections = []
            for sections_type_0_item_data in self.sections:
                sections_type_0_item = sections_type_0_item_data.to_dict()
                sections.append(sections_type_0_item)


        else:
            sections = self.sections

        title = self.title

        author = self.author

        cover_asset_id = self.cover_asset_id

        description = self.description

        edition = self.edition

        editor = self.editor

        isbn = self.isbn

        publication_date = self.publication_date

        publisher = self.publisher

        subtitle = self.subtitle


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "entries": entries,
            "kind": kind,
            "sections": sections,
            "title": title,
        })
        if author is not UNSET:
            field_dict["author"] = author
        if cover_asset_id is not UNSET:
            field_dict["cover_asset_id"] = cover_asset_id
        if description is not UNSET:
            field_dict["description"] = description
        if edition is not UNSET:
            field_dict["edition"] = edition
        if editor is not UNSET:
            field_dict["editor"] = editor
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if publication_date is not UNSET:
            field_dict["publication_date"] = publication_date
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_entry_input import BookEntryInput # noqa: PLC0415
        from ..models.book_section import BookSection # noqa: PLC0415
        d = dict(src_dict)
        def _parse_entries(data: object) -> list[BookEntryInput] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entries_type_0 = []
                _entries_type_0 = data
                for entries_type_0_item_data in (_entries_type_0):
                    entries_type_0_item = BookEntryInput.from_dict(entries_type_0_item_data)



                    entries_type_0.append(entries_type_0_item)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BookEntryInput] | None, data)

        entries = _parse_entries(d.pop("entries"))


        kind = BookInputKind(d.pop("kind"))




        def _parse_sections(data: object) -> list[BookSection] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sections_type_0 = []
                _sections_type_0 = data
                for sections_type_0_item_data in (_sections_type_0):
                    sections_type_0_item = BookSection.from_dict(sections_type_0_item_data)



                    sections_type_0.append(sections_type_0_item)

                return sections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BookSection] | None, data)

        sections = _parse_sections(d.pop("sections"))


        title = d.pop("title")

        author = d.pop("author", UNSET)

        cover_asset_id = d.pop("cover_asset_id", UNSET)

        description = d.pop("description", UNSET)

        edition = d.pop("edition", UNSET)

        editor = d.pop("editor", UNSET)

        isbn = d.pop("isbn", UNSET)

        publication_date = d.pop("publication_date", UNSET)

        publisher = d.pop("publisher", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        book_input = cls(
            entries=entries,
            kind=kind,
            sections=sections,
            title=title,
            author=author,
            cover_asset_id=cover_asset_id,
            description=description,
            edition=edition,
            editor=editor,
            isbn=isbn,
            publication_date=publication_date,
            publisher=publisher,
            subtitle=subtitle,
        )

        return book_input

