from enum import StrEnum

class NormalizationReview(StrEnum):
    CONFIRMED = "confirmed"
    CORRECTED = "corrected"

    def __str__(self) -> str:
        return str(self.value)
