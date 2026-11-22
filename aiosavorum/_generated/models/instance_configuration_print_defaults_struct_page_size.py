from enum import StrEnum

class InstanceConfigurationPrintDefaultsStructPageSize(StrEnum):
    A4 = "a4"
    AUTOMATIC = "automatic"
    LETTER = "letter"

    def __str__(self) -> str:
        return str(self.value)
