from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.assistant_approval_request_access import AssistantApprovalRequestAccess






T = TypeVar("T", bound="AssistantApprovalRequest")



@_attrs_define
class AssistantApprovalRequest:
    """ 
        Attributes:
            access (AssistantApprovalRequestAccess):
            code (str):
            deny (bool):
            library_id (str):
            remember (bool):
     """

    access: AssistantApprovalRequestAccess
    code: str
    deny: bool
    library_id: str
    remember: bool





    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        code = self.code

        deny = self.deny

        library_id = self.library_id

        remember = self.remember


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "access": access,
            "code": code,
            "deny": deny,
            "library_id": library_id,
            "remember": remember,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = AssistantApprovalRequestAccess(d.pop("access"))




        code = d.pop("code")

        deny = d.pop("deny")

        library_id = d.pop("library_id")

        remember = d.pop("remember")

        assistant_approval_request = cls(
            access=access,
            code=code,
            deny=deny,
            library_id=library_id,
            remember=remember,
        )

        return assistant_approval_request

