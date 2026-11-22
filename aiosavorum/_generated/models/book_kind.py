from enum import StrEnum

class BookKind(StrEnum):
    PERSONAL = "personal"
    PUBLICATION = "publication"

    def __str__(self) -> str:
        return str(self.value)
