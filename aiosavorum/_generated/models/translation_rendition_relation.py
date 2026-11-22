from enum import StrEnum

class TranslationRenditionRelation(StrEnum):
    ALTERNATE = "alternate"
    ORIGINAL = "original"
    TRANSLATION = "translation"

    def __str__(self) -> str:
        return str(self.value)
