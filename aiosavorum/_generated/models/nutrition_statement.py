from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.nutrient import Nutrient
  from ..models.nutrition_basis import NutritionBasis





T = TypeVar("T", bound="NutritionStatement")



@_attrs_define
class NutritionStatement:
    """ 
        Attributes:
            basis (NutritionBasis):
            nutrients (list[Nutrient] | None):
            note (str | Unset): Authored qualification of the whole statement
     """

    basis: NutritionBasis
    nutrients: list[Nutrient] | None
    note: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.nutrient import Nutrient # noqa: PLC0415
        from ..models.nutrition_basis import NutritionBasis # noqa: PLC0415
        basis = self.basis.to_dict()

        nutrients: list[dict[str, Any]] | None
        if isinstance(self.nutrients, list):
            nutrients = []
            for nutrients_type_0_item_data in self.nutrients:
                nutrients_type_0_item = nutrients_type_0_item_data.to_dict()
                nutrients.append(nutrients_type_0_item)


        else:
            nutrients = self.nutrients

        note = self.note


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "basis": basis,
            "nutrients": nutrients,
        })
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nutrient import Nutrient # noqa: PLC0415
        from ..models.nutrition_basis import NutritionBasis # noqa: PLC0415
        d = dict(src_dict)
        basis = NutritionBasis.from_dict(d.pop("basis"))




        def _parse_nutrients(data: object) -> list[Nutrient] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nutrients_type_0 = []
                _nutrients_type_0 = data
                for nutrients_type_0_item_data in (_nutrients_type_0):
                    nutrients_type_0_item = Nutrient.from_dict(nutrients_type_0_item_data)



                    nutrients_type_0.append(nutrients_type_0_item)

                return nutrients_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Nutrient] | None, data)

        nutrients = _parse_nutrients(d.pop("nutrients"))


        note = d.pop("note", UNSET)

        nutrition_statement = cls(
            basis=basis,
            nutrients=nutrients,
            note=note,
        )

        return nutrition_statement

