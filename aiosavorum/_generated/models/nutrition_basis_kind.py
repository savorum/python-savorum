from enum import StrEnum

class NutritionBasisKind(StrEnum):
    QUANTITY = "quantity"
    RECIPE = "recipe"
    SERVING = "serving"
    UNSPECIFIED = "unspecified"

    def __str__(self) -> str:
        return str(self.value)
