from enum import StrEnum

class RecipeAuthorCandidateMatch(StrEnum):
    ACCENT = "accent"
    EXACT = "exact"
    FUZZY = "fuzzy"

    def __str__(self) -> str:
        return str(self.value)
