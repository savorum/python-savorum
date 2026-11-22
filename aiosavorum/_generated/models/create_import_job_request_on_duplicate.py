from enum import StrEnum

class CreateImportJobRequestOnDuplicate(StrEnum):
    REJECT = "reject"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
