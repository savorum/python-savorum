from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.quantity_kind import QuantityKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.alternative_option import AlternativeOption
  from ..models.amount import Amount
  from ..models.simple_quantity import SimpleQuantity





T = TypeVar("T", bound="Quantity")



@_attrs_define
class Quantity:
    """ 
        Attributes:
            kind (QuantityKind):
            amount (Amount | Unset):
            options (list[AlternativeOption] | None | Unset):
            terms (list[SimpleQuantity] | None | Unset):
            text (str | Unset):
            unit (str | Unset):
     """

    kind: QuantityKind
    amount: Amount | Unset = UNSET
    options: list[AlternativeOption] | None | Unset = UNSET
    terms: list[SimpleQuantity] | None | Unset = UNSET
    text: str | Unset = UNSET
    unit: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.alternative_option import AlternativeOption # noqa: PLC0415
        from ..models.amount import Amount # noqa: PLC0415
        from ..models.simple_quantity import SimpleQuantity # noqa: PLC0415
        kind = self.kind.value

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)


        else:
            options = self.options

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

        text = self.text

        unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if options is not UNSET:
            field_dict["options"] = options
        if terms is not UNSET:
            field_dict["terms"] = terms
        if text is not UNSET:
            field_dict["text"] = text
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alternative_option import AlternativeOption # noqa: PLC0415
        from ..models.amount import Amount # noqa: PLC0415
        from ..models.simple_quantity import SimpleQuantity # noqa: PLC0415
        d = dict(src_dict)
        kind = QuantityKind(d.pop("kind"))




        _amount = d.pop("amount", UNSET)
        amount: Amount | Unset
        if isinstance(_amount,  Unset):
            amount = UNSET
        else:
            amount = Amount.from_dict(_amount)




        def _parse_options(data: object) -> list[AlternativeOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in (_options_type_0):
                    options_type_0_item = AlternativeOption.from_dict(options_type_0_item_data)



                    options_type_0.append(options_type_0_item)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AlternativeOption] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


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


        text = d.pop("text", UNSET)

        unit = d.pop("unit", UNSET)

        quantity = cls(
            kind=kind,
            amount=amount,
            options=options,
            terms=terms,
            text=text,
            unit=unit,
        )

        return quantity

