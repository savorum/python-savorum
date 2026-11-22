from enum import StrEnum

class ImportInputOnDuplicate(StrEnum):
    REJECT = "reject"
    REPLACE = "replace"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
