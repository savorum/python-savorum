from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.book_kind import BookKind
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.book_entry import BookEntry
  from ..models.book_section import BookSection





T = TypeVar("T", bound="Book")



@_attrs_define
class Book:
    """ 
        Attributes:
            created_at (datetime.datetime):
            entries (list[BookEntry] | None):
            id (str):
            kind (BookKind):
            revision (int):
            sections (list[BookSection] | None):
            title (str):
            updated_at (datetime.datetime):
            author (str | Unset):
            cover_asset_id (str | Unset):
            deleted_at (datetime.datetime | Unset):
            description (str | Unset):
            edition (str | Unset):
            editor (str | Unset):
            isbn (str | Unset):
            preview_asset_id (str | Unset):
            preview_entry_id (str | Unset):
            publication_date (str | Unset):
            publisher (str | Unset):
            subtitle (str | Unset):
     """

    created_at: datetime.datetime
    entries: list[BookEntry] | None
    id: str
    kind: BookKind
    revision: int
    sections: list[BookSection] | None
    title: str
    updated_at: datetime.datetime
    author: str | Unset = UNSET
    cover_asset_id: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    edition: str | Unset = UNSET
    editor: str | Unset = UNSET
    isbn: str | Unset = UNSET
    preview_asset_id: str | Unset = UNSET
    preview_entry_id: str | Unset = UNSET
    publication_date: str | Unset = UNSET
    publisher: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.book_entry import BookEntry # noqa: PLC0415
        from ..models.book_section import BookSection # noqa: PLC0415
        created_at = self.created_at.isoformat()

        entries: list[dict[str, Any]] | None
        if isinstance(self.entries, list):
            entries = []
            for entries_type_0_item_data in self.entries:
                entries_type_0_item = entries_type_0_item_data.to_dict()
                entries.append(entries_type_0_item)


        else:
            entries = self.entries

        id = self.id

        kind = self.kind.value

        revision = self.revision

        sections: list[dict[str, Any]] | None
        if isinstance(self.sections, list):
            sections = []
            for sections_type_0_item_data in self.sections:
                sections_type_0_item = sections_type_0_item_data.to_dict()
                sections.append(sections_type_0_item)


        else:
            sections = self.sections

        title = self.title

        updated_at = self.updated_at.isoformat()

        author = self.author

        cover_asset_id = self.cover_asset_id

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        description = self.description

        edition = self.edition

        editor = self.editor

        isbn = self.isbn

        preview_asset_id = self.preview_asset_id

        preview_entry_id = self.preview_entry_id

        publication_date = self.publication_date

        publisher = self.publisher

        subtitle = self.subtitle


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "entries": entries,
            "id": id,
            "kind": kind,
            "revision": revision,
            "sections": sections,
            "title": title,
            "updated_at": updated_at,
        })
        if author is not UNSET:
            field_dict["author"] = author
        if cover_asset_id is not UNSET:
            field_dict["cover_asset_id"] = cover_asset_id
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if edition is not UNSET:
            field_dict["edition"] = edition
        if editor is not UNSET:
            field_dict["editor"] = editor
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if preview_asset_id is not UNSET:
            field_dict["preview_asset_id"] = preview_asset_id
        if preview_entry_id is not UNSET:
            field_dict["preview_entry_id"] = preview_entry_id
        if publication_date is not UNSET:
            field_dict["publication_date"] = publication_date
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_entry import BookEntry # noqa: PLC0415
        from ..models.book_section import BookSection # noqa: PLC0415
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        def _parse_entries(data: object) -> list[BookEntry] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entries_type_0 = []
                _entries_type_0 = data
                for entries_type_0_item_data in (_entries_type_0):
                    entries_type_0_item = BookEntry.from_dict(entries_type_0_item_data)



                    entries_type_0.append(entries_type_0_item)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BookEntry] | None, data)

        entries = _parse_entries(d.pop("entries"))


        id = d.pop("id")

        kind = BookKind(d.pop("kind"))




        revision = d.pop("revision")

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

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        author = d.pop("author", UNSET)

        cover_asset_id = d.pop("cover_asset_id", UNSET)

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at,  Unset):
            deleted_at = UNSET
        else:
            deleted_at = datetime.datetime.fromisoformat(_deleted_at)




        description = d.pop("description", UNSET)

        edition = d.pop("edition", UNSET)

        editor = d.pop("editor", UNSET)

        isbn = d.pop("isbn", UNSET)

        preview_asset_id = d.pop("preview_asset_id", UNSET)

        preview_entry_id = d.pop("preview_entry_id", UNSET)

        publication_date = d.pop("publication_date", UNSET)

        publisher = d.pop("publisher", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        book = cls(
            created_at=created_at,
            entries=entries,
            id=id,
            kind=kind,
            revision=revision,
            sections=sections,
            title=title,
            updated_at=updated_at,
            author=author,
            cover_asset_id=cover_asset_id,
            deleted_at=deleted_at,
            description=description,
            edition=edition,
            editor=editor,
            isbn=isbn,
            preview_asset_id=preview_asset_id,
            preview_entry_id=preview_entry_id,
            publication_date=publication_date,
            publisher=publisher,
            subtitle=subtitle,
        )


        book.additional_properties = d
        return book

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
