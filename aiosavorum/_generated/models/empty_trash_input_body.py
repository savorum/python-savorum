from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.empty_trash_target import EmptyTrashTarget





T = TypeVar("T", bound="EmptyTrashInputBody")



@_attrs_define
class EmptyTrashInputBody:
    """ 
        Attributes:
            books (list[EmptyTrashTarget] | None | Unset): Trashed books reviewed for permanent removal
            recipes (list[EmptyTrashTarget] | None | Unset): Trashed recipes reviewed for permanent removal
     """

    books: list[EmptyTrashTarget] | None | Unset = UNSET
    recipes: list[EmptyTrashTarget] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.empty_trash_target import EmptyTrashTarget # noqa: PLC0415
        books: list[dict[str, Any]] | None | Unset
        if isinstance(self.books, Unset):
            books = UNSET
        elif isinstance(self.books, list):
            books = []
            for books_type_0_item_data in self.books:
                books_type_0_item = books_type_0_item_data.to_dict()
                books.append(books_type_0_item)


        else:
            books = self.books

        recipes: list[dict[str, Any]] | None | Unset
        if isinstance(self.recipes, Unset):
            recipes = UNSET
        elif isinstance(self.recipes, list):
            recipes = []
            for recipes_type_0_item_data in self.recipes:
                recipes_type_0_item = recipes_type_0_item_data.to_dict()
                recipes.append(recipes_type_0_item)


        else:
            recipes = self.recipes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if books is not UNSET:
            field_dict["books"] = books
        if recipes is not UNSET:
            field_dict["recipes"] = recipes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.empty_trash_target import EmptyTrashTarget # noqa: PLC0415
        d = dict(src_dict)
        def _parse_books(data: object) -> list[EmptyTrashTarget] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                books_type_0 = []
                _books_type_0 = data
                for books_type_0_item_data in (_books_type_0):
                    books_type_0_item = EmptyTrashTarget.from_dict(books_type_0_item_data)



                    books_type_0.append(books_type_0_item)

                return books_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EmptyTrashTarget] | None | Unset, data)

        books = _parse_books(d.pop("books", UNSET))


        def _parse_recipes(data: object) -> list[EmptyTrashTarget] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recipes_type_0 = []
                _recipes_type_0 = data
                for recipes_type_0_item_data in (_recipes_type_0):
                    recipes_type_0_item = EmptyTrashTarget.from_dict(recipes_type_0_item_data)



                    recipes_type_0.append(recipes_type_0_item)

                return recipes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EmptyTrashTarget] | None | Unset, data)

        recipes = _parse_recipes(d.pop("recipes", UNSET))


        empty_trash_input_body = cls(
            books=books,
            recipes=recipes,
        )

        return empty_trash_input_body

