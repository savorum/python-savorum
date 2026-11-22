from enum import StrEnum

class FacetInputKind(StrEnum):
    COURSE = "course"
    CUISINE = "cuisine"
    DIETARY = "dietary"
    METHOD = "method"

    def __str__(self) -> str:
        return str(self.value)
