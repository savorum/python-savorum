from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.attempt import Attempt
  from ..models.delivery import Delivery





T = TypeVar("T", bound="Detail")



@_attrs_define
class Detail:
    """ 
        Attributes:
            attempts (list[Attempt] | None):
            delivery (Delivery):
     """

    attempts: list[Attempt] | None
    delivery: Delivery
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.attempt import Attempt # noqa: PLC0415
        from ..models.delivery import Delivery # noqa: PLC0415
        attempts: list[dict[str, Any]] | None
        if isinstance(self.attempts, list):
            attempts = []
            for attempts_type_0_item_data in self.attempts:
                attempts_type_0_item = attempts_type_0_item_data.to_dict()
                attempts.append(attempts_type_0_item)


        else:
            attempts = self.attempts

        delivery = self.delivery.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "attempts": attempts,
            "delivery": delivery,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attempt import Attempt # noqa: PLC0415
        from ..models.delivery import Delivery # noqa: PLC0415
        d = dict(src_dict)
        def _parse_attempts(data: object) -> list[Attempt] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attempts_type_0 = []
                _attempts_type_0 = data
                for attempts_type_0_item_data in (_attempts_type_0):
                    attempts_type_0_item = Attempt.from_dict(attempts_type_0_item_data)



                    attempts_type_0.append(attempts_type_0_item)

                return attempts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Attempt] | None, data)

        attempts = _parse_attempts(d.pop("attempts"))


        delivery = Delivery.from_dict(d.pop("delivery"))




        detail = cls(
            attempts=attempts,
            delivery=delivery,
        )


        detail.additional_properties = d
        return detail

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
