from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.interface_locale import InterfaceLocale
  from ..models.preference_values import PreferenceValues





T = TypeVar("T", bound="UserPreferences")



@_attrs_define
class UserPreferences:
    """ 
        Attributes:
            effective (PreferenceValues):
            interface_locales (list[InterfaceLocale] | None): Interface languages this server ships. A preview locale is
                incomplete or unreviewed and is used only when chosen explicitly
            overrides (PreferenceValues):
            revision (int):
            version (int):
     """

    effective: PreferenceValues
    interface_locales: list[InterfaceLocale] | None
    overrides: PreferenceValues
    revision: int
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.interface_locale import InterfaceLocale # noqa: PLC0415
        from ..models.preference_values import PreferenceValues # noqa: PLC0415
        effective = self.effective.to_dict()

        interface_locales: list[dict[str, Any]] | None
        if isinstance(self.interface_locales, list):
            interface_locales = []
            for interface_locales_type_0_item_data in self.interface_locales:
                interface_locales_type_0_item = interface_locales_type_0_item_data.to_dict()
                interface_locales.append(interface_locales_type_0_item)


        else:
            interface_locales = self.interface_locales

        overrides = self.overrides.to_dict()

        revision = self.revision

        version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "effective": effective,
            "interface_locales": interface_locales,
            "overrides": overrides,
            "revision": revision,
            "version": version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interface_locale import InterfaceLocale # noqa: PLC0415
        from ..models.preference_values import PreferenceValues # noqa: PLC0415
        d = dict(src_dict)
        effective = PreferenceValues.from_dict(d.pop("effective"))




        def _parse_interface_locales(data: object) -> list[InterfaceLocale] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                interface_locales_type_0 = []
                _interface_locales_type_0 = data
                for interface_locales_type_0_item_data in (_interface_locales_type_0):
                    interface_locales_type_0_item = InterfaceLocale.from_dict(interface_locales_type_0_item_data)



                    interface_locales_type_0.append(interface_locales_type_0_item)

                return interface_locales_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InterfaceLocale] | None, data)

        interface_locales = _parse_interface_locales(d.pop("interface_locales"))


        overrides = PreferenceValues.from_dict(d.pop("overrides"))




        revision = d.pop("revision")

        version = d.pop("version")

        user_preferences = cls(
            effective=effective,
            interface_locales=interface_locales,
            overrides=overrides,
            revision=revision,
            version=version,
        )


        user_preferences.additional_properties = d
        return user_preferences

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
