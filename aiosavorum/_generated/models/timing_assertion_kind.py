from enum import StrEnum

class TimingAssertionKind(StrEnum):
    BRINE = "brine"
    CHILL = "chill"
    COOK = "cook"
    COOL = "cool"
    CURE = "cure"
    DRAIN = "drain"
    FERMENT = "ferment"
    FREEZE = "freeze"
    MARINATE = "marinate"
    OTHER = "other"
    PREP = "prep"
    PROOF = "proof"
    REST = "rest"
    SOAK = "soak"

    def __str__(self) -> str:
        return str(self.value)
