from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.duration_expression import DurationExpression
  from ..models.timing_assertion import TimingAssertion





T = TypeVar("T", bound="Times")



@_attrs_define
class Times:
    """ 
        Attributes:
            additional (DurationExpression | Unset):
            assertions (list[TimingAssertion] | None | Unset):
            cook (DurationExpression | Unset):
            prep (DurationExpression | Unset):
            total (DurationExpression | Unset):
     """

    additional: DurationExpression | Unset = UNSET
    assertions: list[TimingAssertion] | None | Unset = UNSET
    cook: DurationExpression | Unset = UNSET
    prep: DurationExpression | Unset = UNSET
    total: DurationExpression | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.duration_expression import DurationExpression # noqa: PLC0415
        from ..models.timing_assertion import TimingAssertion # noqa: PLC0415
        additional: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional, Unset):
            additional = self.additional.to_dict()

        assertions: list[dict[str, Any]] | None | Unset
        if isinstance(self.assertions, Unset):
            assertions = UNSET
        elif isinstance(self.assertions, list):
            assertions = []
            for assertions_type_0_item_data in self.assertions:
                assertions_type_0_item = assertions_type_0_item_data.to_dict()
                assertions.append(assertions_type_0_item)


        else:
            assertions = self.assertions

        cook: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cook, Unset):
            cook = self.cook.to_dict()

        prep: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prep, Unset):
            prep = self.prep.to_dict()

        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if additional is not UNSET:
            field_dict["additional"] = additional
        if assertions is not UNSET:
            field_dict["assertions"] = assertions
        if cook is not UNSET:
            field_dict["cook"] = cook
        if prep is not UNSET:
            field_dict["prep"] = prep
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duration_expression import DurationExpression # noqa: PLC0415
        from ..models.timing_assertion import TimingAssertion # noqa: PLC0415
        d = dict(src_dict)
        _additional = d.pop("additional", UNSET)
        additional: DurationExpression | Unset
        if isinstance(_additional,  Unset):
            additional = UNSET
        else:
            additional = DurationExpression.from_dict(_additional)




        def _parse_assertions(data: object) -> list[TimingAssertion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assertions_type_0 = []
                _assertions_type_0 = data
                for assertions_type_0_item_data in (_assertions_type_0):
                    assertions_type_0_item = TimingAssertion.from_dict(assertions_type_0_item_data)



                    assertions_type_0.append(assertions_type_0_item)

                return assertions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TimingAssertion] | None | Unset, data)

        assertions = _parse_assertions(d.pop("assertions", UNSET))


        _cook = d.pop("cook", UNSET)
        cook: DurationExpression | Unset
        if isinstance(_cook,  Unset):
            cook = UNSET
        else:
            cook = DurationExpression.from_dict(_cook)




        _prep = d.pop("prep", UNSET)
        prep: DurationExpression | Unset
        if isinstance(_prep,  Unset):
            prep = UNSET
        else:
            prep = DurationExpression.from_dict(_prep)




        _total = d.pop("total", UNSET)
        total: DurationExpression | Unset
        if isinstance(_total,  Unset):
            total = UNSET
        else:
            total = DurationExpression.from_dict(_total)




        times = cls(
            additional=additional,
            assertions=assertions,
            cook=cook,
            prep=prep,
            total=total,
        )

        return times

