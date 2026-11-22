from enum import StrEnum

class ListRecipesState(StrEnum):
    ACTIVE = "active"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
