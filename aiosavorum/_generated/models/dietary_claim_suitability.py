from enum import StrEnum

class DietaryClaimSuitability(StrEnum):
    SUITABLE = "suitable"
    UNSUITABLE = "unsuitable"

    def __str__(self) -> str:
        return str(self.value)
