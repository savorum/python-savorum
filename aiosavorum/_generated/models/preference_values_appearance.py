from enum import StrEnum

class PreferenceValuesAppearance(StrEnum):
    DARK = "dark"
    LIGHT = "light"
    SYSTEM = "system"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
