from enum import StrEnum

class ImportJobItemResourceErrorCode(StrEnum):
    ALREADY_IN_LIBRARY = "already-in-library"
    CHANGED_SINCE_REVIEW = "changed-since-review"
    SOURCE_UNAVAILABLE = "source-unavailable"

    def __str__(self) -> str:
        return str(self.value)
