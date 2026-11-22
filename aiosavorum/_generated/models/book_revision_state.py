from enum import StrEnum

class BookRevisionState(StrEnum):
    ACTIVE = "active"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
