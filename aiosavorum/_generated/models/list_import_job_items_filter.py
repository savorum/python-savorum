from enum import StrEnum

class ListImportJobItemsFilter(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    IMPORTED = "imported"
    INFORMATIONAL = "informational"
    PENDING = "pending"
    REVIEW_REQUIRED = "review-required"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
