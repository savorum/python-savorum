from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.instance_configuration_default_measurement import InstanceConfigurationDefaultMeasurement
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.instance_configuration_capabilities_struct import InstanceConfigurationCapabilitiesStruct
  from ..models.instance_configuration_import_policy_struct import InstanceConfigurationImportPolicyStruct
  from ..models.instance_configuration_print_defaults_struct import InstanceConfigurationPrintDefaultsStruct





T = TypeVar("T", bound="InstanceConfiguration")



@_attrs_define
class InstanceConfiguration:
    """ 
        Attributes:
            capabilities (InstanceConfigurationCapabilitiesStruct):
            default_locale (str):
            default_measurement (InstanceConfigurationDefaultMeasurement):
            display_name (str):
            import_policy (InstanceConfigurationImportPolicyStruct):
            print_defaults (InstanceConfigurationPrintDefaultsStruct):
            public_url (str | Unset):
     """

    capabilities: InstanceConfigurationCapabilitiesStruct
    default_locale: str
    default_measurement: InstanceConfigurationDefaultMeasurement
    display_name: str
    import_policy: InstanceConfigurationImportPolicyStruct
    print_defaults: InstanceConfigurationPrintDefaultsStruct
    public_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.instance_configuration_capabilities_struct import InstanceConfigurationCapabilitiesStruct # noqa: PLC0415
        from ..models.instance_configuration_import_policy_struct import InstanceConfigurationImportPolicyStruct # noqa: PLC0415
        from ..models.instance_configuration_print_defaults_struct import InstanceConfigurationPrintDefaultsStruct # noqa: PLC0415
        capabilities = self.capabilities.to_dict()

        default_locale = self.default_locale

        default_measurement = self.default_measurement.value

        display_name = self.display_name

        import_policy = self.import_policy.to_dict()

        print_defaults = self.print_defaults.to_dict()

        public_url = self.public_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "capabilities": capabilities,
            "default_locale": default_locale,
            "default_measurement": default_measurement,
            "display_name": display_name,
            "import_policy": import_policy,
            "print_defaults": print_defaults,
        })
        if public_url is not UNSET:
            field_dict["public_url"] = public_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instance_configuration_capabilities_struct import InstanceConfigurationCapabilitiesStruct # noqa: PLC0415
        from ..models.instance_configuration_import_policy_struct import InstanceConfigurationImportPolicyStruct # noqa: PLC0415
        from ..models.instance_configuration_print_defaults_struct import InstanceConfigurationPrintDefaultsStruct # noqa: PLC0415
        d = dict(src_dict)
        capabilities = InstanceConfigurationCapabilitiesStruct.from_dict(d.pop("capabilities"))




        default_locale = d.pop("default_locale")

        default_measurement = InstanceConfigurationDefaultMeasurement(d.pop("default_measurement"))




        display_name = d.pop("display_name")

        import_policy = InstanceConfigurationImportPolicyStruct.from_dict(d.pop("import_policy"))




        print_defaults = InstanceConfigurationPrintDefaultsStruct.from_dict(d.pop("print_defaults"))




        public_url = d.pop("public_url", UNSET)

        instance_configuration = cls(
            capabilities=capabilities,
            default_locale=default_locale,
            default_measurement=default_measurement,
            display_name=display_name,
            import_policy=import_policy,
            print_defaults=print_defaults,
            public_url=public_url,
        )


        instance_configuration.additional_properties = d
        return instance_configuration

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
