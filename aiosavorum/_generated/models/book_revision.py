from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.book_revision_cause import BookRevisionCause
from ..models.book_revision_state import BookRevisionState
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.book import Book





T = TypeVar("T", bound="BookRevision")



@_attrs_define
class BookRevision:
    """ 
        Attributes:
            book (Book):
            cause (BookRevisionCause):
            created_at (datetime.datetime):
            state (BookRevisionState):
            actor_id (str | Unset):
            actor_name (str | Unset):
            source_revision (int | Unset):
     """

    book: Book
    cause: BookRevisionCause
    created_at: datetime.datetime
    state: BookRevisionState
    actor_id: str | Unset = UNSET
    actor_name: str | Unset = UNSET
    source_revision: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.book import Book # noqa: PLC0415
        book = self.book.to_dict()

        cause = self.cause.value

        created_at = self.created_at.isoformat()

        state = self.state.value

        actor_id = self.actor_id

        actor_name = self.actor_name

        source_revision = self.source_revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "book": book,
            "cause": cause,
            "created_at": created_at,
            "state": state,
        })
        if actor_id is not UNSET:
            field_dict["actor_id"] = actor_id
        if actor_name is not UNSET:
            field_dict["actor_name"] = actor_name
        if source_revision is not UNSET:
            field_dict["source_revision"] = source_revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.book import Book # noqa: PLC0415
        d = dict(src_dict)
        book = Book.from_dict(d.pop("book"))




        cause = BookRevisionCause(d.pop("cause"))




        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        state = BookRevisionState(d.pop("state"))




        actor_id = d.pop("actor_id", UNSET)

        actor_name = d.pop("actor_name", UNSET)

        source_revision = d.pop("source_revision", UNSET)

        book_revision = cls(
            book=book,
            cause=cause,
            created_at=created_at,
            state=state,
            actor_id=actor_id,
            actor_name=actor_name,
            source_revision=source_revision,
        )


        book_revision.additional_properties = d
        return book_revision

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
