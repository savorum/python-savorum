from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.capability_adapter import CapabilityAdapter
  from ..models.capability_auth_method import CapabilityAuthMethod
  from ..models.capability_limits import CapabilityLimits
  from ..models.capability_links import CapabilityLinks
  from ..models.capability_token import CapabilityToken





T = TypeVar("T", bound="Capabilities")



@_attrs_define
class Capabilities:
    """ 
        Attributes:
            api_major (int):
            auth_enabled (bool):
            auth_methods (list[CapabilityAuthMethod] | None):
            links (CapabilityLinks):
            product (str):
            schema_version (int):
            version (str):
            auth_features (list[str] | None | Unset):
            event_types (list[str] | None | Unset):
            exporters (list[CapabilityAdapter] | None | Unset):
            features (list[str] | None | Unset):
            importers (list[CapabilityAdapter] | None | Unset):
            limits (CapabilityLimits | Unset):
            sref_read (list[str] | None | Unset):
            sref_write (list[str] | None | Unset):
            token (CapabilityToken | Unset):
     """

    api_major: int
    auth_enabled: bool
    auth_methods: list[CapabilityAuthMethod] | None
    links: CapabilityLinks
    product: str
    schema_version: int
    version: str
    auth_features: list[str] | None | Unset = UNSET
    event_types: list[str] | None | Unset = UNSET
    exporters: list[CapabilityAdapter] | None | Unset = UNSET
    features: list[str] | None | Unset = UNSET
    importers: list[CapabilityAdapter] | None | Unset = UNSET
    limits: CapabilityLimits | Unset = UNSET
    sref_read: list[str] | None | Unset = UNSET
    sref_write: list[str] | None | Unset = UNSET
    token: CapabilityToken | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.capability_adapter import CapabilityAdapter # noqa: PLC0415
        from ..models.capability_auth_method import CapabilityAuthMethod # noqa: PLC0415
        from ..models.capability_limits import CapabilityLimits # noqa: PLC0415
        from ..models.capability_links import CapabilityLinks # noqa: PLC0415
        from ..models.capability_token import CapabilityToken # noqa: PLC0415
        api_major = self.api_major

        auth_enabled = self.auth_enabled

        auth_methods: list[dict[str, Any]] | None
        if isinstance(self.auth_methods, list):
            auth_methods = []
            for auth_methods_type_0_item_data in self.auth_methods:
                auth_methods_type_0_item = auth_methods_type_0_item_data.to_dict()
                auth_methods.append(auth_methods_type_0_item)


        else:
            auth_methods = self.auth_methods

        links = self.links.to_dict()

        product = self.product

        schema_version = self.schema_version

        version = self.version

        auth_features: list[str] | None | Unset
        if isinstance(self.auth_features, Unset):
            auth_features = UNSET
        elif isinstance(self.auth_features, list):
            auth_features = self.auth_features


        else:
            auth_features = self.auth_features

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = self.event_types


        else:
            event_types = self.event_types

        exporters: list[dict[str, Any]] | None | Unset
        if isinstance(self.exporters, Unset):
            exporters = UNSET
        elif isinstance(self.exporters, list):
            exporters = []
            for exporters_type_0_item_data in self.exporters:
                exporters_type_0_item = exporters_type_0_item_data.to_dict()
                exporters.append(exporters_type_0_item)


        else:
            exporters = self.exporters

        features: list[str] | None | Unset
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, list):
            features = self.features


        else:
            features = self.features

        importers: list[dict[str, Any]] | None | Unset
        if isinstance(self.importers, Unset):
            importers = UNSET
        elif isinstance(self.importers, list):
            importers = []
            for importers_type_0_item_data in self.importers:
                importers_type_0_item = importers_type_0_item_data.to_dict()
                importers.append(importers_type_0_item)


        else:
            importers = self.importers

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        sref_read: list[str] | None | Unset
        if isinstance(self.sref_read, Unset):
            sref_read = UNSET
        elif isinstance(self.sref_read, list):
            sref_read = self.sref_read


        else:
            sref_read = self.sref_read

        sref_write: list[str] | None | Unset
        if isinstance(self.sref_write, Unset):
            sref_write = UNSET
        elif isinstance(self.sref_write, list):
            sref_write = self.sref_write


        else:
            sref_write = self.sref_write

        token: dict[str, Any] | Unset = UNSET
        if not isinstance(self.token, Unset):
            token = self.token.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "api_major": api_major,
            "auth_enabled": auth_enabled,
            "auth_methods": auth_methods,
            "links": links,
            "product": product,
            "schema_version": schema_version,
            "version": version,
        })
        if auth_features is not UNSET:
            field_dict["auth_features"] = auth_features
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if exporters is not UNSET:
            field_dict["exporters"] = exporters
        if features is not UNSET:
            field_dict["features"] = features
        if importers is not UNSET:
            field_dict["importers"] = importers
        if limits is not UNSET:
            field_dict["limits"] = limits
        if sref_read is not UNSET:
            field_dict["sref_read"] = sref_read
        if sref_write is not UNSET:
            field_dict["sref_write"] = sref_write
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_adapter import CapabilityAdapter # noqa: PLC0415
        from ..models.capability_auth_method import CapabilityAuthMethod # noqa: PLC0415
        from ..models.capability_limits import CapabilityLimits # noqa: PLC0415
        from ..models.capability_links import CapabilityLinks # noqa: PLC0415
        from ..models.capability_token import CapabilityToken # noqa: PLC0415
        d = dict(src_dict)
        api_major = d.pop("api_major")

        auth_enabled = d.pop("auth_enabled")

        def _parse_auth_methods(data: object) -> list[CapabilityAuthMethod] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                auth_methods_type_0 = []
                _auth_methods_type_0 = data
                for auth_methods_type_0_item_data in (_auth_methods_type_0):
                    auth_methods_type_0_item = CapabilityAuthMethod.from_dict(auth_methods_type_0_item_data)



                    auth_methods_type_0.append(auth_methods_type_0_item)

                return auth_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CapabilityAuthMethod] | None, data)

        auth_methods = _parse_auth_methods(d.pop("auth_methods"))


        links = CapabilityLinks.from_dict(d.pop("links"))




        product = d.pop("product")

        schema_version = d.pop("schema_version")

        version = d.pop("version")

        def _parse_auth_features(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                auth_features_type_0 = cast(list[str], data)

                return auth_features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        auth_features = _parse_auth_features(d.pop("auth_features", UNSET))


        def _parse_event_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        event_types = _parse_event_types(d.pop("event_types", UNSET))


        def _parse_exporters(data: object) -> list[CapabilityAdapter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exporters_type_0 = []
                _exporters_type_0 = data
                for exporters_type_0_item_data in (_exporters_type_0):
                    exporters_type_0_item = CapabilityAdapter.from_dict(exporters_type_0_item_data)



                    exporters_type_0.append(exporters_type_0_item)

                return exporters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CapabilityAdapter] | None | Unset, data)

        exporters = _parse_exporters(d.pop("exporters", UNSET))


        def _parse_features(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                features_type_0 = cast(list[str], data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        features = _parse_features(d.pop("features", UNSET))


        def _parse_importers(data: object) -> list[CapabilityAdapter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                importers_type_0 = []
                _importers_type_0 = data
                for importers_type_0_item_data in (_importers_type_0):
                    importers_type_0_item = CapabilityAdapter.from_dict(importers_type_0_item_data)



                    importers_type_0.append(importers_type_0_item)

                return importers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CapabilityAdapter] | None | Unset, data)

        importers = _parse_importers(d.pop("importers", UNSET))


        _limits = d.pop("limits", UNSET)
        limits: CapabilityLimits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = CapabilityLimits.from_dict(_limits)




        def _parse_sref_read(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sref_read_type_0 = cast(list[str], data)

                return sref_read_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        sref_read = _parse_sref_read(d.pop("sref_read", UNSET))


        def _parse_sref_write(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sref_write_type_0 = cast(list[str], data)

                return sref_write_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        sref_write = _parse_sref_write(d.pop("sref_write", UNSET))


        _token = d.pop("token", UNSET)
        token: CapabilityToken | Unset
        if isinstance(_token,  Unset):
            token = UNSET
        else:
            token = CapabilityToken.from_dict(_token)




        capabilities = cls(
            api_major=api_major,
            auth_enabled=auth_enabled,
            auth_methods=auth_methods,
            links=links,
            product=product,
            schema_version=schema_version,
            version=version,
            auth_features=auth_features,
            event_types=event_types,
            exporters=exporters,
            features=features,
            importers=importers,
            limits=limits,
            sref_read=sref_read,
            sref_write=sref_write,
            token=token,
        )


        capabilities.additional_properties = d
        return capabilities

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
