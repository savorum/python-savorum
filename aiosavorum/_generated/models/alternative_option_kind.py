from enum import StrEnum

class AlternativeOptionKind(StrEnum):
    SIMPLE = "simple"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
