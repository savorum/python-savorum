from enum import StrEnum

class NutrientNutrient(StrEnum):
    CARBOHYDRATE = "carbohydrate"
    CHOLESTEROL = "cholesterol"
    ENERGY = "energy"
    FAT = "fat"
    FIBER = "fiber"
    OTHER = "other"
    PROTEIN = "protein"
    SALT = "salt"
    SATURATED_FAT = "saturated_fat"
    SODIUM = "sodium"
    SUGARS = "sugars"
    TRANS_FAT = "trans_fat"
    UNSATURATED_FAT = "unsaturated_fat"

    def __str__(self) -> str:
        return str(self.value)
