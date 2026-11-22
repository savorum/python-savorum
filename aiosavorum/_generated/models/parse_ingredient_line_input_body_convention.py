from enum import StrEnum

class ParseIngredientLineInputBodyConvention(StrEnum):
    AU = "au"
    IMPERIAL = "imperial"
    METRIC = "metric"
    US = "us"

    def __str__(self) -> str:
        return str(self.value)
