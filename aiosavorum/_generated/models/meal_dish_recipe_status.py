from enum import StrEnum

class MealDishRecipeStatus(StrEnum):
    AVAILABLE = "available"
    REMOVED = "removed"
    TRASHED = "trashed"

    def __str__(self) -> str:
        return str(self.value)
