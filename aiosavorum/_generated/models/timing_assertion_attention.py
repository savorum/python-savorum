from enum import StrEnum

class TimingAssertionAttention(StrEnum):
    ACTIVE = "active"
    PASSIVE = "passive"

    def __str__(self) -> str:
        return str(self.value)
