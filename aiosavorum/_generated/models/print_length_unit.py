from enum import StrEnum

class PrintLengthUnit(StrEnum):
    IN = "in"
    MM = "mm"
    PT = "pt"

    def __str__(self) -> str:
        return str(self.value)
