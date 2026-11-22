from enum import StrEnum

class HealthOutputBodyStatus(StrEnum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
