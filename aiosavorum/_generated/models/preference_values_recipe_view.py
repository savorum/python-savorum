from enum import StrEnum

class PreferenceValuesRecipeView(StrEnum):
    COMFORTABLE = "comfortable"
    COMPACT = "compact"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
