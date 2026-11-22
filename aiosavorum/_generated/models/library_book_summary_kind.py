from enum import StrEnum

class LibraryBookSummaryKind(StrEnum):
    PERSONAL = "personal"
    PUBLICATION = "publication"

    def __str__(self) -> str:
        return str(self.value)
