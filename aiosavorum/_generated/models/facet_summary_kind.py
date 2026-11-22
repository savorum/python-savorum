from enum import StrEnum

class FacetSummaryKind(StrEnum):
    COURSE = "course"
    CUISINE = "cuisine"
    DIETARY = "dietary"
    METHOD = "method"

    def __str__(self) -> str:
        return str(self.value)
