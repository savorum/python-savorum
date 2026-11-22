from enum import StrEnum

class LinkTranslationInputBodyRelation(StrEnum):
    ALTERNATE = "alternate"
    ORIGINAL = "original"
    TRANSLATION = "translation"

    def __str__(self) -> str:
        return str(self.value)
