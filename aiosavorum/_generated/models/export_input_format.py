from enum import StrEnum

class ExportInputFormat(StrEnum):
    SREF = "sref"
    SREF_BUNDLE = "sref-bundle"

    def __str__(self) -> str:
        return str(self.value)
