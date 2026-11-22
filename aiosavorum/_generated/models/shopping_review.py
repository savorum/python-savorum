from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shopping_requirement import ShoppingRequirement
  from ..models.shopping_source import ShoppingSource





T = TypeVar("T", bound="ShoppingReview")



@_attrs_define
class ShoppingReview:
    """ 
        Attributes:
            removed (list[ShoppingSource] | None):
            requirements (list[ShoppingRequirement] | None):
            revision (int):
            token (str):
            outdated (bool | Unset):
     """

    removed: list[ShoppingSource] | None
    requirements: list[ShoppingRequirement] | None
    revision: int
    token: str
    outdated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shopping_requirement import ShoppingRequirement # noqa: PLC0415
        from ..models.shopping_source import ShoppingSource # noqa: PLC0415
        removed: list[dict[str, Any]] | None
        if isinstance(self.removed, list):
            removed = []
            for removed_type_0_item_data in self.removed:
                removed_type_0_item = removed_type_0_item_data.to_dict()
                removed.append(removed_type_0_item)


        else:
            removed = self.removed

        requirements: list[dict[str, Any]] | None
        if isinstance(self.requirements, list):
            requirements = []
            for requirements_type_0_item_data in self.requirements:
                requirements_type_0_item = requirements_type_0_item_data.to_dict()
                requirements.append(requirements_type_0_item)


        else:
            requirements = self.requirements

        revision = self.revision

        token = self.token

        outdated = self.outdated


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "removed": removed,
            "requirements": requirements,
            "revision": revision,
            "token": token,
        })
        if outdated is not UNSET:
            field_dict["outdated"] = outdated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shopping_requirement import ShoppingRequirement # noqa: PLC0415
        from ..models.shopping_source import ShoppingSource # noqa: PLC0415
        d = dict(src_dict)
        def _parse_removed(data: object) -> list[ShoppingSource] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                removed_type_0 = []
                _removed_type_0 = data
                for removed_type_0_item_data in (_removed_type_0):
                    removed_type_0_item = ShoppingSource.from_dict(removed_type_0_item_data)



                    removed_type_0.append(removed_type_0_item)

                return removed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShoppingSource] | None, data)

        removed = _parse_removed(d.pop("removed"))


        def _parse_requirements(data: object) -> list[ShoppingRequirement] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requirements_type_0 = []
                _requirements_type_0 = data
                for requirements_type_0_item_data in (_requirements_type_0):
                    requirements_type_0_item = ShoppingRequirement.from_dict(requirements_type_0_item_data)



                    requirements_type_0.append(requirements_type_0_item)

                return requirements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShoppingRequirement] | None, data)

        requirements = _parse_requirements(d.pop("requirements"))


        revision = d.pop("revision")

        token = d.pop("token")

        outdated = d.pop("outdated", UNSET)

        shopping_review = cls(
            removed=removed,
            requirements=requirements,
            revision=revision,
            token=token,
            outdated=outdated,
        )


        shopping_review.additional_properties = d
        return shopping_review

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
