from enum import StrEnum

class AuthorKind(StrEnum):
    ORGANIZATION = "organization"
    OTHER = "other"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
