from enum import StrEnum

class BookSummaryKind(StrEnum):
    PERSONAL = "personal"
    PUBLICATION = "publication"

    def __str__(self) -> str:
        return str(self.value)
