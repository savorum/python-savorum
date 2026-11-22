from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.delete_account_request_confirmation import DeleteAccountRequestConfirmation
from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteAccountRequest")



@_attrs_define
class DeleteAccountRequest:
    """ 
        Attributes:
            confirmation (DeleteAccountRequestConfirmation):
            password (str | Unset):
     """

    confirmation: DeleteAccountRequestConfirmation
    password: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        confirmation = self.confirmation.value

        password = self.password


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "confirmation": confirmation,
        })
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmation = DeleteAccountRequestConfirmation(d.pop("confirmation"))




        password = d.pop("password", UNSET)

        delete_account_request = cls(
            confirmation=confirmation,
            password=password,
        )

        return delete_account_request

