from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.calendar_feed import CalendarFeed





T = TypeVar("T", bound="CalendarFeedSecret")



@_attrs_define
class CalendarFeedSecret:
    """ 
        Attributes:
            feed (CalendarFeed):
            path (str):
            url (str | Unset):
     """

    feed: CalendarFeed
    path: str
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.calendar_feed import CalendarFeed # noqa: PLC0415
        feed = self.feed.to_dict()

        path = self.path

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "feed": feed,
            "path": path,
        })
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_feed import CalendarFeed # noqa: PLC0415
        d = dict(src_dict)
        feed = CalendarFeed.from_dict(d.pop("feed"))




        path = d.pop("path")

        url = d.pop("url", UNSET)

        calendar_feed_secret = cls(
            feed=feed,
            path=path,
            url=url,
        )


        calendar_feed_secret.additional_properties = d
        return calendar_feed_secret

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
