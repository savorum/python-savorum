from enum import StrEnum

class ImportJobItemResourceState(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    IMPORTED = "imported"
    PENDING = "pending"
    RUNNING = "running"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
