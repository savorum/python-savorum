from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_authentication_providers_response_200_providers_item_kind import ListAuthenticationProvidersResponse200ProvidersItemKind
from ..types import UNSET, Unset






T = TypeVar("T", bound="ListAuthenticationProvidersResponse200ProvidersItem")



@_attrs_define
class ListAuthenticationProvidersResponse200ProvidersItem:
    """ 
        Attributes:
            display_name (str):
            id (str):
            kind (ListAuthenticationProvidersResponse200ProvidersItemKind):
            account_origin (str | Unset): Managed provider account origin from trusted deployment configuration.
            tenant_id (str | Unset):
     """

    display_name: str
    id: str
    kind: ListAuthenticationProvidersResponse200ProvidersItemKind
    account_origin: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        id = self.id

        kind = self.kind.value

        account_origin = self.account_origin

        tenant_id = self.tenant_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "display_name": display_name,
            "id": id,
            "kind": kind,
        })
        if account_origin is not UNSET:
            field_dict["account_origin"] = account_origin
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        id = d.pop("id")

        kind = ListAuthenticationProvidersResponse200ProvidersItemKind(d.pop("kind"))




        account_origin = d.pop("account_origin", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        list_authentication_providers_response_200_providers_item = cls(
            display_name=display_name,
            id=id,
            kind=kind,
            account_origin=account_origin,
            tenant_id=tenant_id,
        )


        list_authentication_providers_response_200_providers_item.additional_properties = d
        return list_authentication_providers_response_200_providers_item

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
