from enum import StrEnum

class ImportPreviewAnalysisStatus(StrEnum):
    AMBIGUOUS = "ambiguous"
    DEFINITE_MATCH = "definite-match"
    LIKELY_DUPLICATE = "likely-duplicate"
    NEW = "new"

    def __str__(self) -> str:
        return str(self.value)
