from enum import StrEnum

class NutrientUnit(StrEnum):
    G = "g"
    KCAL = "kcal"
    KJ = "kJ"
    MCG = "mcg"
    MG = "mg"

    def __str__(self) -> str:
        return str(self.value)
