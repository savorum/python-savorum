from enum import StrEnum

class AssetRole(StrEnum):
    IMAGE = "image"
    OTHER = "other"
    SOURCE = "source"

    def __str__(self) -> str:
        return str(self.value)
