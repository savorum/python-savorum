from enum import StrEnum

class TimingAssertionProvenance(StrEnum):
    DERIVED = "derived"
    SUPPLEMENTAL = "supplemental"

    def __str__(self) -> str:
        return str(self.value)
