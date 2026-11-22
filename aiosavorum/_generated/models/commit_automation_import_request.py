from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.commit_automation_import_request_policy import CommitAutomationImportRequestPolicy






T = TypeVar("T", bound="CommitAutomationImportRequest")



@_attrs_define
class CommitAutomationImportRequest:
    """ 
        Attributes:
            policy (CommitAutomationImportRequestPolicy):
     """

    policy: CommitAutomationImportRequestPolicy





    def to_dict(self) -> dict[str, Any]:
        policy = self.policy.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "policy": policy,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy = CommitAutomationImportRequestPolicy(d.pop("policy"))




        commit_automation_import_request = cls(
            policy=policy,
        )

        return commit_automation_import_request

