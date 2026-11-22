from enum import StrEnum

class PreferenceValuesTemperature(StrEnum):
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"
    ORIGINAL = "original"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
