from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_user_request_role import CreateUserRequestRole
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateUserRequest")



@_attrs_define
class CreateUserRequest:
    """ 
        Attributes:
            display_name (str):
            login (str):
            password (str):
            library_id (str | Unset):
            role (CreateUserRequestRole | Unset):
     """

    display_name: str
    login: str
    password: str
    library_id: str | Unset = UNSET
    role: CreateUserRequestRole | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        login = self.login

        password = self.password

        library_id = self.library_id

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "display_name": display_name,
            "login": login,
            "password": password,
        })
        if library_id is not UNSET:
            field_dict["library_id"] = library_id
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        login = d.pop("login")

        password = d.pop("password")

        library_id = d.pop("library_id", UNSET)

        _role = d.pop("role", UNSET)
        role: CreateUserRequestRole | Unset
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = CreateUserRequestRole(_role)




        create_user_request = cls(
            display_name=display_name,
            login=login,
            password=password,
            library_id=library_id,
            role=role,
        )

        return create_user_request

