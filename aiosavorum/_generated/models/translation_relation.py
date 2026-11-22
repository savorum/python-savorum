from enum import StrEnum

class TranslationRelation(StrEnum):
    ALTERNATE = "alternate"
    ORIGINAL = "original"
    TRANSLATION = "translation"

    def __str__(self) -> str:
        return str(self.value)
