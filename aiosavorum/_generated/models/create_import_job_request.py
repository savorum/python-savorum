from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_import_job_request_kind import CreateImportJobRequestKind
from ..models.create_import_job_request_on_duplicate import CreateImportJobRequestOnDuplicate
from ..models.create_import_job_request_policy import CreateImportJobRequestPolicy
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateImportJobRequest")



@_attrs_define
class CreateImportJobRequest:
    """ 
        Attributes:
            kind (CreateImportJobRequestKind):
            file_content (str | Unset):
            filename (str | Unset):
            on_duplicate (CreateImportJobRequestOnDuplicate | Unset):  Default: CreateImportJobRequestOnDuplicate.REJECT.
            policy (CreateImportJobRequestPolicy | Unset):  Default: CreateImportJobRequestPolicy.PREVIEW_ONLY.
            text (str | Unset):
            url (str | Unset):
     """

    kind: CreateImportJobRequestKind
    file_content: str | Unset = UNSET
    filename: str | Unset = UNSET
    on_duplicate: CreateImportJobRequestOnDuplicate | Unset = CreateImportJobRequestOnDuplicate.REJECT
    policy: CreateImportJobRequestPolicy | Unset = CreateImportJobRequestPolicy.PREVIEW_ONLY
    text: str | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        file_content = self.file_content

        filename = self.filename

        on_duplicate: str | Unset = UNSET
        if not isinstance(self.on_duplicate, Unset):
            on_duplicate = self.on_duplicate.value


        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value


        text = self.text

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })
        if file_content is not UNSET:
            field_dict["file_content"] = file_content
        if filename is not UNSET:
            field_dict["filename"] = filename
        if on_duplicate is not UNSET:
            field_dict["on_duplicate"] = on_duplicate
        if policy is not UNSET:
            field_dict["policy"] = policy
        if text is not UNSET:
            field_dict["text"] = text
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = CreateImportJobRequestKind(d.pop("kind"))




        file_content = d.pop("file_content", UNSET)

        filename = d.pop("filename", UNSET)

        _on_duplicate = d.pop("on_duplicate", UNSET)
        on_duplicate: CreateImportJobRequestOnDuplicate | Unset
        if isinstance(_on_duplicate,  Unset):
            on_duplicate = UNSET
        else:
            on_duplicate = CreateImportJobRequestOnDuplicate(_on_duplicate)




        _policy = d.pop("policy", UNSET)
        policy: CreateImportJobRequestPolicy | Unset
        if isinstance(_policy,  Unset):
            policy = UNSET
        else:
            policy = CreateImportJobRequestPolicy(_policy)




        text = d.pop("text", UNSET)

        url = d.pop("url", UNSET)

        create_import_job_request = cls(
            kind=kind,
            file_content=file_content,
            filename=filename,
            on_duplicate=on_duplicate,
            policy=policy,
            text=text,
            url=url,
        )

        return create_import_job_request

