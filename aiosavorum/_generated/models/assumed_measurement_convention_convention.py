from enum import StrEnum

class AssumedMeasurementConventionConvention(StrEnum):
    AU = "au"
    IMPERIAL = "imperial"
    METRIC = "metric"
    US = "us"

    def __str__(self) -> str:
        return str(self.value)
