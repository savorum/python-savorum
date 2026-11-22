from enum import StrEnum

class MeasurementResolutionInterpretationInputConvention(StrEnum):
    AU = "au"
    IMPERIAL = "imperial"
    METRIC = "metric"
    US = "us"

    def __str__(self) -> str:
        return str(self.value)
