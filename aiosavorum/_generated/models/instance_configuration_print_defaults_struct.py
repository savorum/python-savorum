from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.instance_configuration_print_defaults_struct_image import InstanceConfigurationPrintDefaultsStructImage
from ..models.instance_configuration_print_defaults_struct_page_size import InstanceConfigurationPrintDefaultsStructPageSize






T = TypeVar("T", bound="InstanceConfigurationPrintDefaultsStruct")



@_attrs_define
class InstanceConfigurationPrintDefaultsStruct:
    """ 
        Attributes:
            image (InstanceConfigurationPrintDefaultsStructImage):
            page_size (InstanceConfigurationPrintDefaultsStructPageSize):
     """

    image: InstanceConfigurationPrintDefaultsStructImage
    page_size: InstanceConfigurationPrintDefaultsStructPageSize
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        image = self.image.value

        page_size = self.page_size.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "image": image,
            "page_size": page_size,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = InstanceConfigurationPrintDefaultsStructImage(d.pop("image"))




        page_size = InstanceConfigurationPrintDefaultsStructPageSize(d.pop("page_size"))




        instance_configuration_print_defaults_struct = cls(
            image=image,
            page_size=page_size,
        )


        instance_configuration_print_defaults_struct.additional_properties = d
        return instance_configuration_print_defaults_struct

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
