from enum import StrEnum

class PreferenceValuesPrintImage(StrEnum):
    AUTOMATIC = "automatic"
    INCLUDE = "include"
    OMIT = "omit"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
