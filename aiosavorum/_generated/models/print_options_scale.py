from enum import StrEnum

class PrintOptionsScale(StrEnum):
    CUSTOM = "custom"
    ORIGINAL = "original"
    PREFERRED = "preferred"

    def __str__(self) -> str:
        return str(self.value)
