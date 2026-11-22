from enum import StrEnum

class PrintOptionsLayout(StrEnum):
    AUTOMATIC = "automatic"
    SIDE_BY_SIDE = "side-by-side"
    STACKED = "stacked"

    def __str__(self) -> str:
        return str(self.value)
