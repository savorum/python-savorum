from enum import StrEnum

class DietaryClaimDiet(StrEnum):
    DIABETIC = "diabetic"
    GLUTEN_FREE = "gluten_free"
    HALAL = "halal"
    HINDU = "hindu"
    KOSHER = "kosher"
    LOW_CALORIE = "low_calorie"
    LOW_FAT = "low_fat"
    LOW_LACTOSE = "low_lactose"
    LOW_SALT = "low_salt"
    VEGAN = "vegan"
    VEGETARIAN = "vegetarian"

    def __str__(self) -> str:
        return str(self.value)
