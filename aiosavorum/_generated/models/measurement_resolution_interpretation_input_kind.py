from enum import StrEnum

class MeasurementResolutionInterpretationInputKind(StrEnum):
    CANONICAL_UNIT = "canonical-unit"
    CONVENTION = "convention"
    KEEP_WRITTEN = "keep-written"

    def __str__(self) -> str:
        return str(self.value)
