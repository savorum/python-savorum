from enum import StrEnum

class CreateNativeLinkTicketBodyCodeChallengeMethod(StrEnum):
    S256 = "S256"

    def __str__(self) -> str:
        return str(self.value)
