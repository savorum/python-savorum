from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_job_resource_on_duplicate import ImportJobResourceOnDuplicate
from ..models.import_job_resource_state import ImportJobResourceState
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.import_job_progress import ImportJobProgress
  from ..models.import_resolution_decision import ImportResolutionDecision





T = TypeVar("T", bound="ImportJobResource")



@_attrs_define
class ImportJobResource:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (str):
            importer (str): The source formats this import came from, in the reader's words
            on_duplicate (ImportJobResourceOnDuplicate):
            progress (ImportJobProgress):
            resolution_decisions (list[ImportResolutionDecision] | None):
            source (str): What was chosen: a filename, several, or the format when there was no file
            state (ImportJobResourceState):
            total_items (int):
            cancellation_requested_at (datetime.datetime | Unset):
            error (str | Unset):
            finished_at (datetime.datetime | Unset):
            lead_title (str | Unset): The title of this job's first recipe, for naming the import by what it brought
            started_at (datetime.datetime | Unset):
     """

    created_at: datetime.datetime
    id: str
    importer: str
    on_duplicate: ImportJobResourceOnDuplicate
    progress: ImportJobProgress
    resolution_decisions: list[ImportResolutionDecision] | None
    source: str
    state: ImportJobResourceState
    total_items: int
    cancellation_requested_at: datetime.datetime | Unset = UNSET
    error: str | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    lead_title: str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_job_progress import ImportJobProgress # noqa: PLC0415
        from ..models.import_resolution_decision import ImportResolutionDecision # noqa: PLC0415
        created_at = self.created_at.isoformat()

        id = self.id

        importer = self.importer

        on_duplicate = self.on_duplicate.value

        progress = self.progress.to_dict()

        resolution_decisions: list[dict[str, Any]] | None
        if isinstance(self.resolution_decisions, list):
            resolution_decisions = []
            for resolution_decisions_type_0_item_data in self.resolution_decisions:
                resolution_decisions_type_0_item = resolution_decisions_type_0_item_data.to_dict()
                resolution_decisions.append(resolution_decisions_type_0_item)


        else:
            resolution_decisions = self.resolution_decisions

        source = self.source

        state = self.state.value

        total_items = self.total_items

        cancellation_requested_at: str | Unset = UNSET
        if not isinstance(self.cancellation_requested_at, Unset):
            cancellation_requested_at = self.cancellation_requested_at.isoformat()

        error = self.error

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        lead_title = self.lead_title

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "importer": importer,
            "on_duplicate": on_duplicate,
            "progress": progress,
            "resolution_decisions": resolution_decisions,
            "source": source,
            "state": state,
            "total_items": total_items,
        })
        if cancellation_requested_at is not UNSET:
            field_dict["cancellation_requested_at"] = cancellation_requested_at
        if error is not UNSET:
            field_dict["error"] = error
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if lead_title is not UNSET:
            field_dict["lead_title"] = lead_title
        if started_at is not UNSET:
            field_dict["started_at"] = started_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_job_progress import ImportJobProgress # noqa: PLC0415
        from ..models.import_resolution_decision import ImportResolutionDecision # noqa: PLC0415
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        importer = d.pop("importer")

        on_duplicate = ImportJobResourceOnDuplicate(d.pop("on_duplicate"))




        progress = ImportJobProgress.from_dict(d.pop("progress"))




        def _parse_resolution_decisions(data: object) -> list[ImportResolutionDecision] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolution_decisions_type_0 = []
                _resolution_decisions_type_0 = data
                for resolution_decisions_type_0_item_data in (_resolution_decisions_type_0):
                    resolution_decisions_type_0_item = ImportResolutionDecision.from_dict(resolution_decisions_type_0_item_data)



                    resolution_decisions_type_0.append(resolution_decisions_type_0_item)

                return resolution_decisions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportResolutionDecision] | None, data)

        resolution_decisions = _parse_resolution_decisions(d.pop("resolution_decisions"))


        source = d.pop("source")

        state = ImportJobResourceState(d.pop("state"))




        total_items = d.pop("total_items")

        _cancellation_requested_at = d.pop("cancellation_requested_at", UNSET)
        cancellation_requested_at: datetime.datetime | Unset
        if isinstance(_cancellation_requested_at,  Unset):
            cancellation_requested_at = UNSET
        else:
            cancellation_requested_at = datetime.datetime.fromisoformat(_cancellation_requested_at)




        error = d.pop("error", UNSET)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at,  Unset):
            finished_at = UNSET
        else:
            finished_at = datetime.datetime.fromisoformat(_finished_at)




        lead_title = d.pop("lead_title", UNSET)

        _started_at = d.pop("started_at", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        import_job_resource = cls(
            created_at=created_at,
            id=id,
            importer=importer,
            on_duplicate=on_duplicate,
            progress=progress,
            resolution_decisions=resolution_decisions,
            source=source,
            state=state,
            total_items=total_items,
            cancellation_requested_at=cancellation_requested_at,
            error=error,
            finished_at=finished_at,
            lead_title=lead_title,
            started_at=started_at,
        )


        import_job_resource.additional_properties = d
        return import_job_resource

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
