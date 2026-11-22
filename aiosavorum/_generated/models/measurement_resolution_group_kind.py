from enum import StrEnum

class MeasurementResolutionGroupKind(StrEnum):
    UNIT_ALIAS = "unit_alias"

    def __str__(self) -> str:
        return str(self.value)
