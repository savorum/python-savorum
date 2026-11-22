from enum import StrEnum

class MealMealType(StrEnum):
    BREAKFAST = "breakfast"
    DINNER = "dinner"
    LUNCH = "lunch"
    SNACK = "snack"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
