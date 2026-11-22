from enum import StrEnum

class NormalizationMethod(StrEnum):
    AUTHORED = "authored"
    EXTRACTED = "extracted"
    INFERRED = "inferred"
    UNRESOLVED = "unresolved"

    def __str__(self) -> str:
        return str(self.value)
