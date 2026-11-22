from enum import StrEnum

class RecipeRevisionSummaryChangesType0Item(StrEnum):
    DESCRIPTION = "description"
    EQUIPMENT = "equipment"
    INGREDIENTS = "ingredients"
    INSTRUCTIONS = "instructions"
    LABELS = "labels"
    LANGUAGE = "language"
    NOTES = "notes"
    OTHER = "other"
    PHOTOS = "photos"
    SOURCE = "source"
    TIMES = "times"
    TITLE = "title"
    TRANSLATIONS = "translations"
    VARIANTS = "variants"
    YIELD = "yield"

    def __str__(self) -> str:
        return str(self.value)
