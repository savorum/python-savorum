from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.shopping_review_input import ShoppingReviewInput
  from ..models.shopping_selection import ShoppingSelection





T = TypeVar("T", bound="ShoppingApplyInput")



@_attrs_define
class ShoppingApplyInput:
    """ 
        Attributes:
            id (str):
            input_ (ShoppingReviewInput):
            selections (list[ShoppingSelection] | None):
            token (str):
     """

    id: str
    input_: ShoppingReviewInput
    selections: list[ShoppingSelection] | None
    token: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.shopping_review_input import ShoppingReviewInput # noqa: PLC0415
        from ..models.shopping_selection import ShoppingSelection # noqa: PLC0415
        id = self.id

        input_ = self.input_.to_dict()

        selections: list[dict[str, Any]] | None
        if isinstance(self.selections, list):
            selections = []
            for selections_type_0_item_data in self.selections:
                selections_type_0_item = selections_type_0_item_data.to_dict()
                selections.append(selections_type_0_item)


        else:
            selections = self.selections

        token = self.token


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "input": input_,
            "selections": selections,
            "token": token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shopping_review_input import ShoppingReviewInput # noqa: PLC0415
        from ..models.shopping_selection import ShoppingSelection # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        input_ = ShoppingReviewInput.from_dict(d.pop("input"))




        def _parse_selections(data: object) -> list[ShoppingSelection] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selections_type_0 = []
                _selections_type_0 = data
                for selections_type_0_item_data in (_selections_type_0):
                    selections_type_0_item = ShoppingSelection.from_dict(selections_type_0_item_data)



                    selections_type_0.append(selections_type_0_item)

                return selections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShoppingSelection] | None, data)

        selections = _parse_selections(d.pop("selections"))


        token = d.pop("token")

        shopping_apply_input = cls(
            id=id,
            input_=input_,
            selections=selections,
            token=token,
        )

        return shopping_apply_input

