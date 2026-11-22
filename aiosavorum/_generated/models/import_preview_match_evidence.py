from enum import StrEnum

class ImportPreviewMatchEvidence(StrEnum):
    CANONICAL_URL = "canonical-url"
    PORTABLE_ID = "portable-id"
    SIMILARITY = "similarity"
    SOURCE_IDENTITY = "source-identity"

    def __str__(self) -> str:
        return str(self.value)
