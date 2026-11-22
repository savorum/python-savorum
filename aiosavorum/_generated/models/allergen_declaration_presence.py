from enum import StrEnum

class AllergenDeclarationPresence(StrEnum):
    CONTAINS = "contains"
    FREE_FROM = "free_from"
    MAY_CONTAIN = "may_contain"

    def __str__(self) -> str:
        return str(self.value)
