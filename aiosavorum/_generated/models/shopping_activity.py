from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.shopping_activity_kind import ShoppingActivityKind
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.shopping_activity_item import ShoppingActivityItem





T = TypeVar("T", bound="ShoppingActivity")



@_attrs_define
class ShoppingActivity:
    """ 
        Attributes:
            actor_id (str):
            actor_name (str):
            created_at (datetime.datetime):
            id (int):
            items (list[ShoppingActivityItem] | None):
            kind (ShoppingActivityKind):
     """

    actor_id: str
    actor_name: str
    created_at: datetime.datetime
    id: int
    items: list[ShoppingActivityItem] | None
    kind: ShoppingActivityKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shopping_activity_item import ShoppingActivityItem # noqa: PLC0415
        actor_id = self.actor_id

        actor_name = self.actor_name

        created_at = self.created_at.isoformat()

        id = self.id

        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        kind = self.kind.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "actor_id": actor_id,
            "actor_name": actor_name,
            "created_at": created_at,
            "id": id,
            "items": items,
            "kind": kind,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shopping_activity_item import ShoppingActivityItem # noqa: PLC0415
        d = dict(src_dict)
        actor_id = d.pop("actor_id")

        actor_name = d.pop("actor_name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        def _parse_items(data: object) -> list[ShoppingActivityItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = ShoppingActivityItem.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShoppingActivityItem] | None, data)

        items = _parse_items(d.pop("items"))


        kind = ShoppingActivityKind(d.pop("kind"))




        shopping_activity = cls(
            actor_id=actor_id,
            actor_name=actor_name,
            created_at=created_at,
            id=id,
            items=items,
            kind=kind,
        )


        shopping_activity.additional_properties = d
        return shopping_activity

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
