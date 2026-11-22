from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.book_membership_input import BookMembershipInput
  from ..models.recipe_source import RecipeSource
  from ..models.user_state import UserState





T = TypeVar("T", bound="OrganizationInput")



@_attrs_define
class OrganizationInput:
    """ 
        Attributes:
            facet_ids (list[str] | None):
            sources (list[RecipeSource] | None):
            tag_ids (list[str] | None):
            user_state (UserState):
            book_membership (list[BookMembershipInput] | None | Unset): Book membership changes applied in the same
                transaction
     """

    facet_ids: list[str] | None
    sources: list[RecipeSource] | None
    tag_ids: list[str] | None
    user_state: UserState
    book_membership: list[BookMembershipInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.book_membership_input import BookMembershipInput # noqa: PLC0415
        from ..models.recipe_source import RecipeSource # noqa: PLC0415
        from ..models.user_state import UserState # noqa: PLC0415
        facet_ids: list[str] | None
        if isinstance(self.facet_ids, list):
            facet_ids = self.facet_ids


        else:
            facet_ids = self.facet_ids

        sources: list[dict[str, Any]] | None
        if isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)


        else:
            sources = self.sources

        tag_ids: list[str] | None
        if isinstance(self.tag_ids, list):
            tag_ids = self.tag_ids


        else:
            tag_ids = self.tag_ids

        user_state = self.user_state.to_dict()

        book_membership: list[dict[str, Any]] | None | Unset
        if isinstance(self.book_membership, Unset):
            book_membership = UNSET
        elif isinstance(self.book_membership, list):
            book_membership = []
            for book_membership_type_0_item_data in self.book_membership:
                book_membership_type_0_item = book_membership_type_0_item_data.to_dict()
                book_membership.append(book_membership_type_0_item)


        else:
            book_membership = self.book_membership


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "facet_ids": facet_ids,
            "sources": sources,
            "tag_ids": tag_ids,
            "user_state": user_state,
        })
        if book_membership is not UNSET:
            field_dict["book_membership"] = book_membership

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book_membership_input import BookMembershipInput # noqa: PLC0415
        from ..models.recipe_source import RecipeSource # noqa: PLC0415
        from ..models.user_state import UserState # noqa: PLC0415
        d = dict(src_dict)
        def _parse_facet_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facet_ids_type_0 = cast(list[str], data)

                return facet_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        facet_ids = _parse_facet_ids(d.pop("facet_ids"))


        def _parse_sources(data: object) -> list[RecipeSource] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in (_sources_type_0):
                    sources_type_0_item = RecipeSource.from_dict(sources_type_0_item_data)



                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RecipeSource] | None, data)

        sources = _parse_sources(d.pop("sources"))


        def _parse_tag_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tag_ids_type_0 = cast(list[str], data)

                return tag_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tag_ids = _parse_tag_ids(d.pop("tag_ids"))


        user_state = UserState.from_dict(d.pop("user_state"))




        def _parse_book_membership(data: object) -> list[BookMembershipInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                book_membership_type_0 = []
                _book_membership_type_0 = data
                for book_membership_type_0_item_data in (_book_membership_type_0):
                    book_membership_type_0_item = BookMembershipInput.from_dict(book_membership_type_0_item_data)



                    book_membership_type_0.append(book_membership_type_0_item)

                return book_membership_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BookMembershipInput] | None | Unset, data)

        book_membership = _parse_book_membership(d.pop("book_membership", UNSET))


        organization_input = cls(
            facet_ids=facet_ids,
            sources=sources,
            tag_ids=tag_ids,
            user_state=user_state,
            book_membership=book_membership,
        )

        return organization_input

