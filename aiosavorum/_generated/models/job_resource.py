from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="JobResource")



@_attrs_define
class JobResource:
    """ 
        Attributes:
            created_at (str):
            finished (int):
            id (str):
            kind (str):
            revision (int):
            state (str):
            total (int):
            code (str | Unset):
            download_url (str | Unset):
            expires_at (str | Unset):
            import_job_id (str | Unset):
     """

    created_at: str
    finished: int
    id: str
    kind: str
    revision: int
    state: str
    total: int
    code: str | Unset = UNSET
    download_url: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    import_job_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        finished = self.finished

        id = self.id

        kind = self.kind

        revision = self.revision

        state = self.state

        total = self.total

        code = self.code

        download_url = self.download_url

        expires_at = self.expires_at

        import_job_id = self.import_job_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "finished": finished,
            "id": id,
            "kind": kind,
            "revision": revision,
            "state": state,
            "total": total,
        })
        if code is not UNSET:
            field_dict["code"] = code
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if import_job_id is not UNSET:
            field_dict["import_job_id"] = import_job_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        finished = d.pop("finished")

        id = d.pop("id")

        kind = d.pop("kind")

        revision = d.pop("revision")

        state = d.pop("state")

        total = d.pop("total")

        code = d.pop("code", UNSET)

        download_url = d.pop("download_url", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        import_job_id = d.pop("import_job_id", UNSET)

        job_resource = cls(
            created_at=created_at,
            finished=finished,
            id=id,
            kind=kind,
            revision=revision,
            state=state,
            total=total,
            code=code,
            download_url=download_url,
            expires_at=expires_at,
            import_job_id=import_job_id,
        )


        job_resource.additional_properties = d
        return job_resource

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
