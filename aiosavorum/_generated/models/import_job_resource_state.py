from enum import StrEnum

class ImportJobResourceState(StrEnum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    COMPLETED_WITH_ERRORS = "completed-with-errors"
    FAILED = "failed"
    INTERRUPTED = "interrupted"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
