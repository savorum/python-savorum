from enum import StrEnum

class RecipeRevisionState(StrEnum):
    ACTIVE = "active"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
