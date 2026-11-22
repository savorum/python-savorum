from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.import_diagnostic import ImportDiagnostic
  from ..models.recipe_document import RecipeDocument





T = TypeVar("T", bound="ImportEventResource")



@_attrs_define
class ImportEventResource:
    """ 
        Attributes:
            baseline_revision (int):
            content_sha256 (str):
            diagnostics (list[ImportDiagnostic] | None):
            display_name (str):
            entry_id (str):
            id (str):
            importer (str):
            importer_version (str):
            input_kind (str):
            operation (str):
            recipe_id (str):
            revision (int):
            timestamp (datetime.datetime):
            actor_id (str | Unset):
            actor_name (str | Unset):
            job_id (str | Unset):
            source_id (str | Unset):
            source_snapshot (RecipeDocument | Unset):
            source_url (str | Unset):
     """

    baseline_revision: int
    content_sha256: str
    diagnostics: list[ImportDiagnostic] | None
    display_name: str
    entry_id: str
    id: str
    importer: str
    importer_version: str
    input_kind: str
    operation: str
    recipe_id: str
    revision: int
    timestamp: datetime.datetime
    actor_id: str | Unset = UNSET
    actor_name: str | Unset = UNSET
    job_id: str | Unset = UNSET
    source_id: str | Unset = UNSET
    source_snapshot: RecipeDocument | Unset = UNSET
    source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_diagnostic import ImportDiagnostic # noqa: PLC0415
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        baseline_revision = self.baseline_revision

        content_sha256 = self.content_sha256

        diagnostics: list[dict[str, Any]] | None
        if isinstance(self.diagnostics, list):
            diagnostics = []
            for diagnostics_type_0_item_data in self.diagnostics:
                diagnostics_type_0_item = diagnostics_type_0_item_data.to_dict()
                diagnostics.append(diagnostics_type_0_item)


        else:
            diagnostics = self.diagnostics

        display_name = self.display_name

        entry_id = self.entry_id

        id = self.id

        importer = self.importer

        importer_version = self.importer_version

        input_kind = self.input_kind

        operation = self.operation

        recipe_id = self.recipe_id

        revision = self.revision

        timestamp = self.timestamp.isoformat()

        actor_id = self.actor_id

        actor_name = self.actor_name

        job_id = self.job_id

        source_id = self.source_id

        source_snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_snapshot, Unset):
            source_snapshot = self.source_snapshot.to_dict()

        source_url = self.source_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "baseline_revision": baseline_revision,
            "content_sha256": content_sha256,
            "diagnostics": diagnostics,
            "display_name": display_name,
            "entry_id": entry_id,
            "id": id,
            "importer": importer,
            "importer_version": importer_version,
            "input_kind": input_kind,
            "operation": operation,
            "recipe_id": recipe_id,
            "revision": revision,
            "timestamp": timestamp,
        })
        if actor_id is not UNSET:
            field_dict["actor_id"] = actor_id
        if actor_name is not UNSET:
            field_dict["actor_name"] = actor_name
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_snapshot is not UNSET:
            field_dict["source_snapshot"] = source_snapshot
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_diagnostic import ImportDiagnostic # noqa: PLC0415
        from ..models.recipe_document import RecipeDocument # noqa: PLC0415
        d = dict(src_dict)
        baseline_revision = d.pop("baseline_revision")

        content_sha256 = d.pop("content_sha256")

        def _parse_diagnostics(data: object) -> list[ImportDiagnostic] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                diagnostics_type_0 = []
                _diagnostics_type_0 = data
                for diagnostics_type_0_item_data in (_diagnostics_type_0):
                    diagnostics_type_0_item = ImportDiagnostic.from_dict(diagnostics_type_0_item_data)



                    diagnostics_type_0.append(diagnostics_type_0_item)

                return diagnostics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportDiagnostic] | None, data)

        diagnostics = _parse_diagnostics(d.pop("diagnostics"))


        display_name = d.pop("display_name")

        entry_id = d.pop("entry_id")

        id = d.pop("id")

        importer = d.pop("importer")

        importer_version = d.pop("importer_version")

        input_kind = d.pop("input_kind")

        operation = d.pop("operation")

        recipe_id = d.pop("recipe_id")

        revision = d.pop("revision")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))




        actor_id = d.pop("actor_id", UNSET)

        actor_name = d.pop("actor_name", UNSET)

        job_id = d.pop("job_id", UNSET)

        source_id = d.pop("source_id", UNSET)

        _source_snapshot = d.pop("source_snapshot", UNSET)
        source_snapshot: RecipeDocument | Unset
        if isinstance(_source_snapshot,  Unset):
            source_snapshot = UNSET
        else:
            source_snapshot = RecipeDocument.from_dict(_source_snapshot)




        source_url = d.pop("source_url", UNSET)

        import_event_resource = cls(
            baseline_revision=baseline_revision,
            content_sha256=content_sha256,
            diagnostics=diagnostics,
            display_name=display_name,
            entry_id=entry_id,
            id=id,
            importer=importer,
            importer_version=importer_version,
            input_kind=input_kind,
            operation=operation,
            recipe_id=recipe_id,
            revision=revision,
            timestamp=timestamp,
            actor_id=actor_id,
            actor_name=actor_name,
            job_id=job_id,
            source_id=source_id,
            source_snapshot=source_snapshot,
            source_url=source_url,
        )


        import_event_resource.additional_properties = d
        return import_event_resource

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
