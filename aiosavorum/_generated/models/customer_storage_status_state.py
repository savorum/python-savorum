from enum import StrEnum

class CustomerStorageStatusState(StrEnum):
    LIMITED = "limited"
    NORMAL = "normal"
    UNKNOWN = "unknown"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
