from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.account_state_user_type_0 import AccountStateUserType0
  from ..models.library import Library





T = TypeVar("T", bound="AccountState")



@_attrs_define
class AccountState:
    """ 
        Attributes:
            active_library_id (str):
            auth_enabled (bool):
            csrf_token (str):
            libraries (list[Library] | None):
            passkeys_available (bool):
            recovery_authenticated (bool):
            user (AccountStateUserType0 | None):
     """

    active_library_id: str
    auth_enabled: bool
    csrf_token: str
    libraries: list[Library] | None
    passkeys_available: bool
    recovery_authenticated: bool
    user: AccountStateUserType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_state_user_type_0 import AccountStateUserType0 # noqa: PLC0415
        from ..models.library import Library # noqa: PLC0415
        active_library_id = self.active_library_id

        auth_enabled = self.auth_enabled

        csrf_token = self.csrf_token

        libraries: list[dict[str, Any]] | None
        if isinstance(self.libraries, list):
            libraries = []
            for libraries_type_0_item_data in self.libraries:
                libraries_type_0_item = libraries_type_0_item_data.to_dict()
                libraries.append(libraries_type_0_item)


        else:
            libraries = self.libraries

        passkeys_available = self.passkeys_available

        recovery_authenticated = self.recovery_authenticated

        user: dict[str, Any] | None
        if isinstance(self.user, AccountStateUserType0):
            user = self.user.to_dict()
        else:
            user = self.user


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "active_library_id": active_library_id,
            "auth_enabled": auth_enabled,
            "csrf_token": csrf_token,
            "libraries": libraries,
            "passkeys_available": passkeys_available,
            "recovery_authenticated": recovery_authenticated,
            "user": user,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_state_user_type_0 import AccountStateUserType0 # noqa: PLC0415
        from ..models.library import Library # noqa: PLC0415
        d = dict(src_dict)
        active_library_id = d.pop("active_library_id")

        auth_enabled = d.pop("auth_enabled")

        csrf_token = d.pop("csrf_token")

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


        passkeys_available = d.pop("passkeys_available")

        recovery_authenticated = d.pop("recovery_authenticated")

        def _parse_user(data: object) -> AccountStateUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = AccountStateUserType0.from_dict(data)



                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountStateUserType0 | None, data)

        user = _parse_user(d.pop("user"))


        account_state = cls(
            active_library_id=active_library_id,
            auth_enabled=auth_enabled,
            csrf_token=csrf_token,
            libraries=libraries,
            passkeys_available=passkeys_available,
            recovery_authenticated=recovery_authenticated,
            user=user,
        )


        account_state.additional_properties = d
        return account_state

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
