from enum import StrEnum

class PreferenceValuesReducedMotion(StrEnum):
    REDUCE = "reduce"
    SYSTEM = "system"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
