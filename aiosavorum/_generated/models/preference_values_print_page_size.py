from enum import StrEnum

class PreferenceValuesPrintPageSize(StrEnum):
    A4 = "a4"
    AUTOMATIC = "automatic"
    LETTER = "letter"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
