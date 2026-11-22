from enum import StrEnum

class PrintOptionsMeasurement(StrEnum):
    AU = "au"
    METRIC = "metric"
    ORIGINAL = "original"
    US = "us"

    def __str__(self) -> str:
        return str(self.value)
