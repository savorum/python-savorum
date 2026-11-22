from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_job_item_resource_error_code import ImportJobItemResourceErrorCode
from ..models.import_job_item_resource_outcome import ImportJobItemResourceOutcome
from ..models.import_job_item_resource_state import ImportJobItemResourceState
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.import_job_diagnostic import ImportJobDiagnostic





T = TypeVar("T", bound="ImportJobItemResource")



@_attrs_define
class ImportJobItemResource:
    """ 
        Attributes:
            deferred_assets (int): Photographs not fetched yet whose addresses the recipe retains
            dropped_assets (int): Photographs this recipe names that could not be retrieved and were left out
            position (int):
            review_required (bool):
            state (ImportJobItemResourceState):
            title (str):
            diagnostics (list[ImportJobDiagnostic] | None | Unset):
            error (str | Unset):
            error_code (ImportJobItemResourceErrorCode | Unset): Why a failed recipe could not be imported, when the cause
                is recognized
            filename (str | Unset):
            finished_at (datetime.datetime | Unset):
            import_event_id (str | Unset):
            library_entry_id (str | Unset):
            outcome (ImportJobItemResourceOutcome | Unset):
            recipe_id (str | Unset):
            revision (int | Unset):
            source_url (str | Unset):
            started_at (datetime.datetime | Unset):
     """

    deferred_assets: int
    dropped_assets: int
    position: int
    review_required: bool
    state: ImportJobItemResourceState
    title: str
    diagnostics: list[ImportJobDiagnostic] | None | Unset = UNSET
    error: str | Unset = UNSET
    error_code: ImportJobItemResourceErrorCode | Unset = UNSET
    filename: str | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    import_event_id: str | Unset = UNSET
    library_entry_id: str | Unset = UNSET
    outcome: ImportJobItemResourceOutcome | Unset = UNSET
    recipe_id: str | Unset = UNSET
    revision: int | Unset = UNSET
    source_url: str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_job_diagnostic import ImportJobDiagnostic # noqa: PLC0415
        deferred_assets = self.deferred_assets

        dropped_assets = self.dropped_assets

        position = self.position

        review_required = self.review_required

        state = self.state.value

        title = self.title

        diagnostics: list[dict[str, Any]] | None | Unset
        if isinstance(self.diagnostics, Unset):
            diagnostics = UNSET
        elif isinstance(self.diagnostics, list):
            diagnostics = []
            for diagnostics_type_0_item_data in self.diagnostics:
                diagnostics_type_0_item = diagnostics_type_0_item_data.to_dict()
                diagnostics.append(diagnostics_type_0_item)


        else:
            diagnostics = self.diagnostics

        error = self.error

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value


        filename = self.filename

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        import_event_id = self.import_event_id

        library_entry_id = self.library_entry_id

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value


        recipe_id = self.recipe_id

        revision = self.revision

        source_url = self.source_url

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "deferred_assets": deferred_assets,
            "dropped_assets": dropped_assets,
            "position": position,
            "review_required": review_required,
            "state": state,
            "title": title,
        })
        if diagnostics is not UNSET:
            field_dict["diagnostics"] = diagnostics
        if error is not UNSET:
            field_dict["error"] = error
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if filename is not UNSET:
            field_dict["filename"] = filename
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if import_event_id is not UNSET:
            field_dict["import_event_id"] = import_event_id
        if library_entry_id is not UNSET:
            field_dict["library_entry_id"] = library_entry_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if recipe_id is not UNSET:
            field_dict["recipe_id"] = recipe_id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if started_at is not UNSET:
            field_dict["started_at"] = started_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_job_diagnostic import ImportJobDiagnostic # noqa: PLC0415
        d = dict(src_dict)
        deferred_assets = d.pop("deferred_assets")

        dropped_assets = d.pop("dropped_assets")

        position = d.pop("position")

        review_required = d.pop("review_required")

        state = ImportJobItemResourceState(d.pop("state"))




        title = d.pop("title")

        def _parse_diagnostics(data: object) -> list[ImportJobDiagnostic] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                diagnostics_type_0 = []
                _diagnostics_type_0 = data
                for diagnostics_type_0_item_data in (_diagnostics_type_0):
                    diagnostics_type_0_item = ImportJobDiagnostic.from_dict(diagnostics_type_0_item_data)



                    diagnostics_type_0.append(diagnostics_type_0_item)

                return diagnostics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportJobDiagnostic] | None | Unset, data)

        diagnostics = _parse_diagnostics(d.pop("diagnostics", UNSET))


        error = d.pop("error", UNSET)

        _error_code = d.pop("error_code", UNSET)
        error_code: ImportJobItemResourceErrorCode | Unset
        if isinstance(_error_code,  Unset):
            error_code = UNSET
        else:
            error_code = ImportJobItemResourceErrorCode(_error_code)




        filename = d.pop("filename", UNSET)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at,  Unset):
            finished_at = UNSET
        else:
            finished_at = datetime.datetime.fromisoformat(_finished_at)




        import_event_id = d.pop("import_event_id", UNSET)

        library_entry_id = d.pop("library_entry_id", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: ImportJobItemResourceOutcome | Unset
        if isinstance(_outcome,  Unset):
            outcome = UNSET
        else:
            outcome = ImportJobItemResourceOutcome(_outcome)




        recipe_id = d.pop("recipe_id", UNSET)

        revision = d.pop("revision", UNSET)

        source_url = d.pop("source_url", UNSET)

        _started_at = d.pop("started_at", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        import_job_item_resource = cls(
            deferred_assets=deferred_assets,
            dropped_assets=dropped_assets,
            position=position,
            review_required=review_required,
            state=state,
            title=title,
            diagnostics=diagnostics,
            error=error,
            error_code=error_code,
            filename=filename,
            finished_at=finished_at,
            import_event_id=import_event_id,
            library_entry_id=library_entry_id,
            outcome=outcome,
            recipe_id=recipe_id,
            revision=revision,
            source_url=source_url,
            started_at=started_at,
        )


        import_job_item_resource.additional_properties = d
        return import_job_item_resource

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
