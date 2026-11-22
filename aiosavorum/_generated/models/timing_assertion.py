from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.timing_assertion_attention import TimingAssertionAttention
from ..models.timing_assertion_kind import TimingAssertionKind
from ..models.timing_assertion_provenance import TimingAssertionProvenance
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.duration_expression import DurationExpression
  from ..models.microwave_conditions import MicrowaveConditions





T = TypeVar("T", bound="TimingAssertion")



@_attrs_define
class TimingAssertion:
    """ 
        Attributes:
            duration (DurationExpression):
            id (str):
            attention (TimingAssertionAttention | Unset): Authored semantics; absent means the recipe does not say
            kind (TimingAssertionKind | Unset): Absent when the source supports a duration but no defensible classification
            label (str | Unset): Required when kind is other; may retitle a named one
            microwave (MicrowaveConditions | Unset):
            note (str | Unset):
            provenance (TimingAssertionProvenance | Unset): How Savorum came to hold this timing; not part of the portable
                recipe
     """

    duration: DurationExpression
    id: str
    attention: TimingAssertionAttention | Unset = UNSET
    kind: TimingAssertionKind | Unset = UNSET
    label: str | Unset = UNSET
    microwave: MicrowaveConditions | Unset = UNSET
    note: str | Unset = UNSET
    provenance: TimingAssertionProvenance | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.duration_expression import DurationExpression # noqa: PLC0415
        from ..models.microwave_conditions import MicrowaveConditions # noqa: PLC0415
        duration = self.duration.to_dict()

        id = self.id

        attention: str | Unset = UNSET
        if not isinstance(self.attention, Unset):
            attention = self.attention.value


        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        label = self.label

        microwave: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microwave, Unset):
            microwave = self.microwave.to_dict()

        note = self.note

        provenance: str | Unset = UNSET
        if not isinstance(self.provenance, Unset):
            provenance = self.provenance.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "duration": duration,
            "id": id,
        })
        if attention is not UNSET:
            field_dict["attention"] = attention
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if microwave is not UNSET:
            field_dict["microwave"] = microwave
        if note is not UNSET:
            field_dict["note"] = note
        if provenance is not UNSET:
            field_dict["provenance"] = provenance

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duration_expression import DurationExpression # noqa: PLC0415
        from ..models.microwave_conditions import MicrowaveConditions # noqa: PLC0415
        d = dict(src_dict)
        duration = DurationExpression.from_dict(d.pop("duration"))




        id = d.pop("id")

        _attention = d.pop("attention", UNSET)
        attention: TimingAssertionAttention | Unset
        if isinstance(_attention,  Unset):
            attention = UNSET
        else:
            attention = TimingAssertionAttention(_attention)




        _kind = d.pop("kind", UNSET)
        kind: TimingAssertionKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = TimingAssertionKind(_kind)




        label = d.pop("label", UNSET)

        _microwave = d.pop("microwave", UNSET)
        microwave: MicrowaveConditions | Unset
        if isinstance(_microwave,  Unset):
            microwave = UNSET
        else:
            microwave = MicrowaveConditions.from_dict(_microwave)




        note = d.pop("note", UNSET)

        _provenance = d.pop("provenance", UNSET)
        provenance: TimingAssertionProvenance | Unset
        if isinstance(_provenance,  Unset):
            provenance = UNSET
        else:
            provenance = TimingAssertionProvenance(_provenance)




        timing_assertion = cls(
            duration=duration,
            id=id,
            attention=attention,
            kind=kind,
            label=label,
            microwave=microwave,
            note=note,
            provenance=provenance,
        )

        return timing_assertion

