from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_job_diagnostic_summary import ImportJobDiagnosticSummary





T = TypeVar("T", bound="ImportJobProgress")



@_attrs_define
class ImportJobProgress:
    """ 
        Attributes:
            cancelled (int):
            current_batch (int): The one-based batch being processed, zero before work starts
            diagnostic_occurrences (int):
            diagnostics (list[ImportJobDiagnosticSummary] | None):
            failed (int):
            finished (int):
            imported (int):
            informational_preservation (int):
            pending (int):
            resumable (int): Unfinished recipes Savorum still holds enough of to run again
            review_required (int):
            running (int):
            skipped (int):
            total (int):
            total_batches (int):
            without_diagnostics (int):
            already_in_library (int | Unset): Failed items recognized as recipes already in the library; included in failed
     """

    cancelled: int
    current_batch: int
    diagnostic_occurrences: int
    diagnostics: list[ImportJobDiagnosticSummary] | None
    failed: int
    finished: int
    imported: int
    informational_preservation: int
    pending: int
    resumable: int
    review_required: int
    running: int
    skipped: int
    total: int
    total_batches: int
    without_diagnostics: int
    already_in_library: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_job_diagnostic_summary import ImportJobDiagnosticSummary # noqa: PLC0415
        cancelled = self.cancelled

        current_batch = self.current_batch

        diagnostic_occurrences = self.diagnostic_occurrences

        diagnostics: list[dict[str, Any]] | None
        if isinstance(self.diagnostics, list):
            diagnostics = []
            for diagnostics_type_0_item_data in self.diagnostics:
                diagnostics_type_0_item = diagnostics_type_0_item_data.to_dict()
                diagnostics.append(diagnostics_type_0_item)


        else:
            diagnostics = self.diagnostics

        failed = self.failed

        finished = self.finished

        imported = self.imported

        informational_preservation = self.informational_preservation

        pending = self.pending

        resumable = self.resumable

        review_required = self.review_required

        running = self.running

        skipped = self.skipped

        total = self.total

        total_batches = self.total_batches

        without_diagnostics = self.without_diagnostics

        already_in_library = self.already_in_library


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cancelled": cancelled,
            "current_batch": current_batch,
            "diagnostic_occurrences": diagnostic_occurrences,
            "diagnostics": diagnostics,
            "failed": failed,
            "finished": finished,
            "imported": imported,
            "informational_preservation": informational_preservation,
            "pending": pending,
            "resumable": resumable,
            "review_required": review_required,
            "running": running,
            "skipped": skipped,
            "total": total,
            "total_batches": total_batches,
            "without_diagnostics": without_diagnostics,
        })
        if already_in_library is not UNSET:
            field_dict["already_in_library"] = already_in_library

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_job_diagnostic_summary import ImportJobDiagnosticSummary # noqa: PLC0415
        d = dict(src_dict)
        cancelled = d.pop("cancelled")

        current_batch = d.pop("current_batch")

        diagnostic_occurrences = d.pop("diagnostic_occurrences")

        def _parse_diagnostics(data: object) -> list[ImportJobDiagnosticSummary] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                diagnostics_type_0 = []
                _diagnostics_type_0 = data
                for diagnostics_type_0_item_data in (_diagnostics_type_0):
                    diagnostics_type_0_item = ImportJobDiagnosticSummary.from_dict(diagnostics_type_0_item_data)



                    diagnostics_type_0.append(diagnostics_type_0_item)

                return diagnostics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImportJobDiagnosticSummary] | None, data)

        diagnostics = _parse_diagnostics(d.pop("diagnostics"))


        failed = d.pop("failed")

        finished = d.pop("finished")

        imported = d.pop("imported")

        informational_preservation = d.pop("informational_preservation")

        pending = d.pop("pending")

        resumable = d.pop("resumable")

        review_required = d.pop("review_required")

        running = d.pop("running")

        skipped = d.pop("skipped")

        total = d.pop("total")

        total_batches = d.pop("total_batches")

        without_diagnostics = d.pop("without_diagnostics")

        already_in_library = d.pop("already_in_library", UNSET)

        import_job_progress = cls(
            cancelled=cancelled,
            current_batch=current_batch,
            diagnostic_occurrences=diagnostic_occurrences,
            diagnostics=diagnostics,
            failed=failed,
            finished=finished,
            imported=imported,
            informational_preservation=informational_preservation,
            pending=pending,
            resumable=resumable,
            review_required=review_required,
            running=running,
            skipped=skipped,
            total=total,
            total_batches=total_batches,
            without_diagnostics=without_diagnostics,
            already_in_library=already_in_library,
        )


        import_job_progress.additional_properties = d
        return import_job_progress

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
