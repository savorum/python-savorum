from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shopping_item import ShoppingItem
  from ..models.shopping_list_requirements import ShoppingListRequirements
  from ..models.shopping_list_selections import ShoppingListSelections





T = TypeVar("T", bound="ShoppingList")



@_attrs_define
class ShoppingList:
    """ 
        Attributes:
            id (str):
            items (list[ShoppingItem] | None):
            name (str):
            requirements (ShoppingListRequirements):
            revision (int):
            selections (ShoppingListSelections):
            applied_revision (int | Unset):
     """

    id: str
    items: list[ShoppingItem] | None
    name: str
    requirements: ShoppingListRequirements
    revision: int
    selections: ShoppingListSelections
    applied_revision: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shopping_item import ShoppingItem # noqa: PLC0415
        from ..models.shopping_list_requirements import ShoppingListRequirements # noqa: PLC0415
        from ..models.shopping_list_selections import ShoppingListSelections # noqa: PLC0415
        id = self.id

        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        name = self.name

        requirements = self.requirements.to_dict()

        revision = self.revision

        selections = self.selections.to_dict()

        applied_revision = self.applied_revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "items": items,
            "name": name,
            "requirements": requirements,
            "revision": revision,
            "selections": selections,
        })
        if applied_revision is not UNSET:
            field_dict["applied_revision"] = applied_revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shopping_item import ShoppingItem # noqa: PLC0415
        from ..models.shopping_list_requirements import ShoppingListRequirements # noqa: PLC0415
        from ..models.shopping_list_selections import ShoppingListSelections # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_items(data: object) -> list[ShoppingItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = ShoppingItem.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShoppingItem] | None, data)

        items = _parse_items(d.pop("items"))


        name = d.pop("name")

        requirements = ShoppingListRequirements.from_dict(d.pop("requirements"))




        revision = d.pop("revision")

        selections = ShoppingListSelections.from_dict(d.pop("selections"))




        applied_revision = d.pop("applied_revision", UNSET)

        shopping_list = cls(
            id=id,
            items=items,
            name=name,
            requirements=requirements,
            revision=revision,
            selections=selections,
            applied_revision=applied_revision,
        )


        shopping_list.additional_properties = d
        return shopping_list

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
