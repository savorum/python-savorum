from enum import StrEnum

class BeginNativeBrowserLoginCodeChallengeMethod(StrEnum):
    S256 = "S256"

    def __str__(self) -> str:
        return str(self.value)
