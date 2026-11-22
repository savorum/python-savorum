from enum import StrEnum

class PrintOptionsOutput(StrEnum):
    NATIVE = "native"
    SHEET_A4 = "sheet-a4"
    SHEET_LETTER = "sheet-letter"

    def __str__(self) -> str:
        return str(self.value)
