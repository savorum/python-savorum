from enum import StrEnum

class PreferenceValuesMeasurement(StrEnum):
    AU = "au"
    METRIC = "metric"
    ORIGINAL = "original"
    US = "us"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
