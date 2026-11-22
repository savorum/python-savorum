from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.library import Library





T = TypeVar("T", bound="LibrariesResponse")



@_attrs_define
class LibrariesResponse:
    """ 
        Attributes:
            libraries (list[Library] | None):
     """

    libraries: list[Library] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.library import Library # noqa: PLC0415
        libraries: list[dict[str, Any]] | None
        if isinstance(self.libraries, list):
            libraries = []
            for libraries_type_0_item_data in self.libraries:
                libraries_type_0_item = libraries_type_0_item_data.to_dict()
                libraries.append(libraries_type_0_item)


        else:
            libraries = self.libraries


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "libraries": libraries,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library import Library # noqa: PLC0415
        d = dict(src_dict)
        def _parse_libraries(data: object) -> list[Library] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                libraries_type_0 = []
                _libraries_type_0 = data
                for libraries_type_0_item_data in (_libraries_type_0):
                    libraries_type_0_item = Library.from_dict(libraries_type_0_item_data)



                    libraries_type_0.append(libraries_type_0_item)

                return libraries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Library] | None, data)

        libraries = _parse_libraries(d.pop("libraries"))


        libraries_response = cls(
            libraries=libraries,
        )


        libraries_response.additional_properties = d
        return libraries_response

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
