from enum import StrEnum

class PrintOptionsImage(StrEnum):
    AUTOMATIC = "automatic"
    INCLUDE = "include"
    OMIT = "omit"

    def __str__(self) -> str:
        return str(self.value)
