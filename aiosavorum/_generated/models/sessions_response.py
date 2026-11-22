from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.account_session import AccountSession





T = TypeVar("T", bound="SessionsResponse")



@_attrs_define
class SessionsResponse:
    """ 
        Attributes:
            sessions (list[AccountSession] | None):
     """

    sessions: list[AccountSession] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_session import AccountSession # noqa: PLC0415
        sessions: list[dict[str, Any]] | None
        if isinstance(self.sessions, list):
            sessions = []
            for sessions_type_0_item_data in self.sessions:
                sessions_type_0_item = sessions_type_0_item_data.to_dict()
                sessions.append(sessions_type_0_item)


        else:
            sessions = self.sessions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sessions": sessions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_session import AccountSession # noqa: PLC0415
        d = dict(src_dict)
        def _parse_sessions(data: object) -> list[AccountSession] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sessions_type_0 = []
                _sessions_type_0 = data
                for sessions_type_0_item_data in (_sessions_type_0):
                    sessions_type_0_item = AccountSession.from_dict(sessions_type_0_item_data)



                    sessions_type_0.append(sessions_type_0_item)

                return sessions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccountSession] | None, data)

        sessions = _parse_sessions(d.pop("sessions"))


        sessions_response = cls(
            sessions=sessions,
        )


        sessions_response.additional_properties = d
        return sessions_response

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
