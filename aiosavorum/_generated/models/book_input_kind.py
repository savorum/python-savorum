from enum import StrEnum

class BookInputKind(StrEnum):
    PERSONAL = "personal"
    PUBLICATION = "publication"

    def __str__(self) -> str:
        return str(self.value)
