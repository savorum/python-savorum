from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.alternative_option_kind import AlternativeOptionKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.amount import Amount
  from ..models.simple_quantity import SimpleQuantity





T = TypeVar("T", bound="AlternativeOption")



@_attrs_define
class AlternativeOption:
    """ 
        Attributes:
            kind (AlternativeOptionKind):
            amount (Amount | Unset):
            terms (list[SimpleQuantity] | None | Unset):
            unit (str | Unset):
     """

    kind: AlternativeOptionKind
    amount: Amount | Unset = UNSET
    terms: list[SimpleQuantity] | None | Unset = UNSET
    unit: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.amount import Amount # noqa: PLC0415
        from ..models.simple_quantity import SimpleQuantity # noqa: PLC0415
        kind = self.kind.value

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        terms: list[dict[str, Any]] | None | Unset
        if isinstance(self.terms, Unset):
            terms = UNSET
        elif isinstance(self.terms, list):
            terms = []
            for terms_type_0_item_data in self.terms:
                terms_type_0_item = terms_type_0_item_data.to_dict()
                terms.append(terms_type_0_item)


        else:
            terms = self.terms

        unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if terms is not UNSET:
            field_dict["terms"] = terms
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount import Amount # noqa: PLC0415
        from ..models.simple_quantity import SimpleQuantity # noqa: PLC0415
        d = dict(src_dict)
        kind = AlternativeOptionKind(d.pop("kind"))




        _amount = d.pop("amount", UNSET)
        amount: Amount | Unset
        if isinstance(_amount,  Unset):
            amount = UNSET
        else:
            amount = Amount.from_dict(_amount)




        def _parse_terms(data: object) -> list[SimpleQuantity] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                terms_type_0 = []
                _terms_type_0 = data
                for terms_type_0_item_data in (_terms_type_0):
                    terms_type_0_item = SimpleQuantity.from_dict(terms_type_0_item_data)



                    terms_type_0.append(terms_type_0_item)

                return terms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleQuantity] | None | Unset, data)

        terms = _parse_terms(d.pop("terms", UNSET))


        unit = d.pop("unit", UNSET)

        alternative_option = cls(
            kind=kind,
            amount=amount,
            terms=terms,
            unit=unit,
        )

        return alternative_option

