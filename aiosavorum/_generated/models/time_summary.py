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





T = TypeVar("T", bound="TimeSummary")



@_attrs_define
class TimeSummary:
    """ 
        Attributes:
            active (DurationExpression | Unset):
            cook (DurationExpression | Unset):
            elapsed (DurationExpression | Unset):
            prep (DurationExpression | Unset):
            written_total (DurationExpression | Unset):
     """

    active: DurationExpression | Unset = UNSET
    cook: DurationExpression | Unset = UNSET
    elapsed: DurationExpression | Unset = UNSET
    prep: DurationExpression | Unset = UNSET
    written_total: DurationExpression | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.duration_expression import DurationExpression # noqa: PLC0415
        active: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        cook: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cook, Unset):
            cook = self.cook.to_dict()

        elapsed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.elapsed, Unset):
            elapsed = self.elapsed.to_dict()

        prep: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prep, Unset):
            prep = self.prep.to_dict()

        written_total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.written_total, Unset):
            written_total = self.written_total.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if active is not UNSET:
            field_dict["active"] = active
        if cook is not UNSET:
            field_dict["cook"] = cook
        if elapsed is not UNSET:
            field_dict["elapsed"] = elapsed
        if prep is not UNSET:
            field_dict["prep"] = prep
        if written_total is not UNSET:
            field_dict["written_total"] = written_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duration_expression import DurationExpression # noqa: PLC0415
        d = dict(src_dict)
        _active = d.pop("active", UNSET)
        active: DurationExpression | Unset
        if isinstance(_active,  Unset):
            active = UNSET
        else:
            active = DurationExpression.from_dict(_active)




        _cook = d.pop("cook", UNSET)
        cook: DurationExpression | Unset
        if isinstance(_cook,  Unset):
            cook = UNSET
        else:
            cook = DurationExpression.from_dict(_cook)




        _elapsed = d.pop("elapsed", UNSET)
        elapsed: DurationExpression | Unset
        if isinstance(_elapsed,  Unset):
            elapsed = UNSET
        else:
            elapsed = DurationExpression.from_dict(_elapsed)




        _prep = d.pop("prep", UNSET)
        prep: DurationExpression | Unset
        if isinstance(_prep,  Unset):
            prep = UNSET
        else:
            prep = DurationExpression.from_dict(_prep)




        _written_total = d.pop("written_total", UNSET)
        written_total: DurationExpression | Unset
        if isinstance(_written_total,  Unset):
            written_total = UNSET
        else:
            written_total = DurationExpression.from_dict(_written_total)




        time_summary = cls(
            active=active,
            cook=cook,
            elapsed=elapsed,
            prep=prep,
            written_total=written_total,
        )


        time_summary.additional_properties = d
        return time_summary

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
