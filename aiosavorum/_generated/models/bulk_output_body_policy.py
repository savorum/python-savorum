from enum import StrEnum

class BulkOutputBodyPolicy(StrEnum):
    PARTIAL_SUCCESS = "partial-success"

    def __str__(self) -> str:
        return str(self.value)
