from enum import StrEnum

class SimpleQuantityKind(StrEnum):
    SIMPLE = "simple"

    def __str__(self) -> str:
        return str(self.value)
