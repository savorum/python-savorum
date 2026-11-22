from enum import StrEnum

class IngredientRelation(StrEnum):
    AND_OR = "and_or"
    OR = "or"
    PREFERRED = "preferred"

    def __str__(self) -> str:
        return str(self.value)
