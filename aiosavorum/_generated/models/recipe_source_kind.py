from enum import StrEnum

class RecipeSourceKind(StrEnum):
    OTHER = "other"
    PUBLICATION = "publication"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
