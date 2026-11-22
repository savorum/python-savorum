from enum import StrEnum

class ImportJobItemResourceOutcome(StrEnum):
    CREATED = "created"
    REPLACED = "replaced"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
