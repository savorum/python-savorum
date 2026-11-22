from enum import StrEnum

class QuantityKind(StrEnum):
    ALTERNATIVES = "alternatives"
    OPAQUE = "opaque"
    SIMPLE = "simple"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
