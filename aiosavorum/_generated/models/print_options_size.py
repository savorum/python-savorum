from enum import StrEnum

class PrintOptionsSize(StrEnum):
    A4 = "a4"
    CARD_3X5 = "card-3x5"
    CARD_4X6 = "card-4x6"
    CARD_5X8 = "card-5x8"
    LETTER = "letter"

    def __str__(self) -> str:
        return str(self.value)
