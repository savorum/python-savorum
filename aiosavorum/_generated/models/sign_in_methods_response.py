from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.sign_in_method import SignInMethod





T = TypeVar("T", bound="SignInMethodsResponse")



@_attrs_define
class SignInMethodsResponse:
    """ 
        Attributes:
            methods (list[SignInMethod] | None):
     """

    methods: list[SignInMethod] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sign_in_method import SignInMethod # noqa: PLC0415
        methods: list[dict[str, Any]] | None
        if isinstance(self.methods, list):
            methods = []
            for methods_type_0_item_data in self.methods:
                methods_type_0_item = methods_type_0_item_data.to_dict()
                methods.append(methods_type_0_item)


        else:
            methods = self.methods


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "methods": methods,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sign_in_method import SignInMethod # noqa: PLC0415
        d = dict(src_dict)
        def _parse_methods(data: object) -> list[SignInMethod] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                methods_type_0 = []
                _methods_type_0 = data
                for methods_type_0_item_data in (_methods_type_0):
                    methods_type_0_item = SignInMethod.from_dict(methods_type_0_item_data)



                    methods_type_0.append(methods_type_0_item)

                return methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SignInMethod] | None, data)

        methods = _parse_methods(d.pop("methods"))


        sign_in_methods_response = cls(
            methods=methods,
        )


        sign_in_methods_response.additional_properties = d
        return sign_in_methods_response

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
