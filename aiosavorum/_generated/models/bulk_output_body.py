from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bulk_output_body_policy import BulkOutputBodyPolicy
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_item_result import BulkItemResult
  from ..models.job_resource import JobResource





T = TypeVar("T", bound="BulkOutputBody")



@_attrs_define
class BulkOutputBody:
    """ 
        Attributes:
            policy (BulkOutputBodyPolicy):
            items (list[BulkItemResult] | None | Unset):
            job (JobResource | Unset):
     """

    policy: BulkOutputBodyPolicy
    items: list[BulkItemResult] | None | Unset = UNSET
    job: JobResource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_item_result import BulkItemResult # noqa: PLC0415
        from ..models.job_resource import JobResource # noqa: PLC0415
        policy = self.policy.value

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "policy": policy,
        })
        if items is not UNSET:
            field_dict["items"] = items
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_item_result import BulkItemResult # noqa: PLC0415
        from ..models.job_resource import JobResource # noqa: PLC0415
        d = dict(src_dict)
        policy = BulkOutputBodyPolicy(d.pop("policy"))




        def _parse_items(data: object) -> list[BulkItemResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = BulkItemResult.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BulkItemResult] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        _job = d.pop("job", UNSET)
        job: JobResource | Unset
        if isinstance(_job,  Unset):
            job = UNSET
        else:
            job = JobResource.from_dict(_job)




        bulk_output_body = cls(
            policy=policy,
            items=items,
            job=job,
        )


        bulk_output_body.additional_properties = d
        return bulk_output_body

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
