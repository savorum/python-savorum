from enum import StrEnum

class TemperaturePurposeKind(StrEnum):
    INTERNAL = "internal"
    OIL = "oil"
    OTHER = "other"
    OVEN = "oven"
    SURFACE = "surface"
    WATER = "water"

    def __str__(self) -> str:
        return str(self.value)
