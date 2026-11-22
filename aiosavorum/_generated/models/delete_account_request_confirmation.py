from enum import StrEnum

class DeleteAccountRequestConfirmation(StrEnum):
    DELETE = "DELETE"

    def __str__(self) -> str:
        return str(self.value)
