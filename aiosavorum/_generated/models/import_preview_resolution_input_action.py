from enum import StrEnum

class ImportPreviewResolutionInputAction(StrEnum):
    SEPARATE = "separate"
    SKIP = "skip"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
