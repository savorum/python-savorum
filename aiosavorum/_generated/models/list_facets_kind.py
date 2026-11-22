from enum import StrEnum

class ListFacetsKind(StrEnum):
    COURSE = "course"
    CUISINE = "cuisine"
    DIETARY = "dietary"
    METHOD = "method"

    def __str__(self) -> str:
        return str(self.value)
