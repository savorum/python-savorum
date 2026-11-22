from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.asset_reference import AssetReference
  from ..models.facet_summary import FacetSummary
  from ..models.library_book_summary import LibraryBookSummary
  from ..models.summary_rendition import SummaryRendition
  from ..models.tag_summary import TagSummary





T = TypeVar("T", bound="RecipeSummary")



@_attrs_define
class RecipeSummary:
    """ 
        Attributes:
            authors (list[str] | None):
            books (list[LibraryBookSummary] | None): Books this recipe was deliberately placed in
            created_at (datetime.datetime):
            favorite (bool):
            id (str): Identifier of this entry in the local Savorum library
            recipe_id (str): Portable recipe document identifier
            revision (int):
            source_books (list[LibraryBookSummary] | None): Publication books this recipe was taken from
            tags (list[TagSummary] | None):
            times_cooked (int): Imported baseline plus this reader's cooking records
            title (str):
            updated_at (datetime.datetime):
            active_time (str | Unset): Derived time this recipe needs the cook
            deleted_at (datetime.datetime | Unset):
            description (str | Unset):
            facets (list[FacetSummary] | None | Unset): Library categories assigned to this recipe
            language (str | Unset): The recipe's primary language as a BCP 47 tag
            last_cooked (datetime.date | Unset): Most recent cooking record
            primary_image (AssetReference | Unset):
            total_time (str | Unset): Derived time from starting to being able to eat
            translations (list[SummaryRendition] | None | Unset): Other renditions of a result grouped by translation;
                present only when grouping was requested
     """

    authors: list[str] | None
    books: list[LibraryBookSummary] | None
    created_at: datetime.datetime
    favorite: bool
    id: str
    recipe_id: str
    revision: int
    source_books: list[LibraryBookSummary] | None
    tags: list[TagSummary] | None
    times_cooked: int
    title: str
    updated_at: datetime.datetime
    active_time: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    facets: list[FacetSummary] | None | Unset = UNSET
    language: str | Unset = UNSET
    last_cooked: datetime.date | Unset = UNSET
    primary_image: AssetReference | Unset = UNSET
    total_time: str | Unset = UNSET
    translations: list[SummaryRendition] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_reference import AssetReference # noqa: PLC0415
        from ..models.facet_summary import FacetSummary # noqa: PLC0415
        from ..models.library_book_summary import LibraryBookSummary # noqa: PLC0415
        from ..models.summary_rendition import SummaryRendition # noqa: PLC0415
        from ..models.tag_summary import TagSummary # noqa: PLC0415
        authors: list[str] | None
        if isinstance(self.authors, list):
            authors = self.authors


        else:
            authors = self.authors

        books: list[dict[str, Any]] | None
        if isinstance(self.books, list):
            books = []
            for books_type_0_item_data in self.books:
                books_type_0_item = books_type_0_item_data.to_dict()
                books.append(books_type_0_item)


        else:
            books = self.books

        created_at = self.created_at.isoformat()

        favorite = self.favorite

        id = self.id

        recipe_id = self.recipe_id

        revision = self.revision

        source_books: list[dict[str, Any]] | None
        if isinstance(self.source_books, list):
            source_books = []
            for source_books_type_0_item_data in self.source_books:
                source_books_type_0_item = source_books_type_0_item_data.to_dict()
                source_books.append(source_books_type_0_item)


        else:
            source_books = self.source_books

        tags: list[dict[str, Any]] | None
        if isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)


        else:
            tags = self.tags

        times_cooked = self.times_cooked

        title = self.title

        updated_at = self.updated_at.isoformat()

        active_time = self.active_time

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        description = self.description

        facets: list[dict[str, Any]] | None | Unset
        if isinstance(self.facets, Unset):
            facets = UNSET
        elif isinstance(self.facets, list):
            facets = []
            for facets_type_0_item_data in self.facets:
                facets_type_0_item = facets_type_0_item_data.to_dict()
                facets.append(facets_type_0_item)


        else:
            facets = self.facets

        language = self.language

        last_cooked: str | Unset = UNSET
        if not isinstance(self.last_cooked, Unset):
            last_cooked = self.last_cooked.isoformat()

        primary_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_image, Unset):
            primary_image = self.primary_image.to_dict()

        total_time = self.total_time

        translations: list[dict[str, Any]] | None | Unset
        if isinstance(self.translations, Unset):
            translations = UNSET
        elif isinstance(self.translations, list):
            translations = []
            for translations_type_0_item_data in self.translations:
                translations_type_0_item = translations_type_0_item_data.to_dict()
                translations.append(translations_type_0_item)


        else:
            translations = self.translations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "authors": authors,
            "books": books,
            "created_at": created_at,
            "favorite": favorite,
            "id": id,
            "recipe_id": recipe_id,
            "revision": revision,
            "source_books": source_books,
            "tags": tags,
            "times_cooked": times_cooked,
            "title": title,
            "updated_at": updated_at,
        })
        if active_time is not UNSET:
            field_dict["active_time"] = active_time
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if facets is not UNSET:
            field_dict["facets"] = facets
        if language is not UNSET:
            field_dict["language"] = language
        if last_cooked is not UNSET:
            field_dict["last_cooked"] = last_cooked
        if primary_image is not UNSET:
            field_dict["primary_image"] = primary_image
        if total_time is not UNSET:
            field_dict["total_time"] = total_time
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_reference import AssetReference # noqa: PLC0415
        from ..models.facet_summary import FacetSummary # noqa: PLC0415
        from ..models.library_book_summary import LibraryBookSummary # noqa: PLC0415
        from ..models.summary_rendition import SummaryRendition # noqa: PLC0415
        from ..models.tag_summary import TagSummary # noqa: PLC0415
        d = dict(src_dict)
        def _parse_authors(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authors_type_0 = cast(list[str], data)

                return authors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        authors = _parse_authors(d.pop("authors"))


        def _parse_books(data: object) -> list[LibraryBookSummary] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                books_type_0 = []
                _books_type_0 = data
                for books_type_0_item_data in (_books_type_0):
                    books_type_0_item = LibraryBookSummary.from_dict(books_type_0_item_data)



                    books_type_0.append(books_type_0_item)

                return books_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LibraryBookSummary] | None, data)

        books = _parse_books(d.pop("books"))


        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        favorite = d.pop("favorite")

        id = d.pop("id")

        recipe_id = d.pop("recipe_id")

        revision = d.pop("revision")

        def _parse_source_books(data: object) -> list[LibraryBookSummary] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_books_type_0 = []
                _source_books_type_0 = data
                for source_books_type_0_item_data in (_source_books_type_0):
                    source_books_type_0_item = LibraryBookSummary.from_dict(source_books_type_0_item_data)



                    source_books_type_0.append(source_books_type_0_item)

                return source_books_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LibraryBookSummary] | None, data)

        source_books = _parse_source_books(d.pop("source_books"))


        def _parse_tags(data: object) -> list[TagSummary] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in (_tags_type_0):
                    tags_type_0_item = TagSummary.from_dict(tags_type_0_item_data)



                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagSummary] | None, data)

        tags = _parse_tags(d.pop("tags"))


        times_cooked = d.pop("times_cooked")

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        active_time = d.pop("active_time", UNSET)

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at,  Unset):
            deleted_at = UNSET
        else:
            deleted_at = datetime.datetime.fromisoformat(_deleted_at)




        description = d.pop("description", UNSET)

        def _parse_facets(data: object) -> list[FacetSummary] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facets_type_0 = []
                _facets_type_0 = data
                for facets_type_0_item_data in (_facets_type_0):
                    facets_type_0_item = FacetSummary.from_dict(facets_type_0_item_data)



                    facets_type_0.append(facets_type_0_item)

                return facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FacetSummary] | None | Unset, data)

        facets = _parse_facets(d.pop("facets", UNSET))


        language = d.pop("language", UNSET)

        _last_cooked = d.pop("last_cooked", UNSET)
        last_cooked: datetime.date | Unset
        if isinstance(_last_cooked,  Unset):
            last_cooked = UNSET
        else:
            last_cooked = datetime.date.fromisoformat(_last_cooked)




        _primary_image = d.pop("primary_image", UNSET)
        primary_image: AssetReference | Unset
        if isinstance(_primary_image,  Unset):
            primary_image = UNSET
        else:
            primary_image = AssetReference.from_dict(_primary_image)




        total_time = d.pop("total_time", UNSET)

        def _parse_translations(data: object) -> list[SummaryRendition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                translations_type_0 = []
                _translations_type_0 = data
                for translations_type_0_item_data in (_translations_type_0):
                    translations_type_0_item = SummaryRendition.from_dict(translations_type_0_item_data)



                    translations_type_0.append(translations_type_0_item)

                return translations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SummaryRendition] | None | Unset, data)

        translations = _parse_translations(d.pop("translations", UNSET))


        recipe_summary = cls(
            authors=authors,
            books=books,
            created_at=created_at,
            favorite=favorite,
            id=id,
            recipe_id=recipe_id,
            revision=revision,
            source_books=source_books,
            tags=tags,
            times_cooked=times_cooked,
            title=title,
            updated_at=updated_at,
            active_time=active_time,
            deleted_at=deleted_at,
            description=description,
            facets=facets,
            language=language,
            last_cooked=last_cooked,
            primary_image=primary_image,
            total_time=total_time,
            translations=translations,
        )


        recipe_summary.additional_properties = d
        return recipe_summary

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
