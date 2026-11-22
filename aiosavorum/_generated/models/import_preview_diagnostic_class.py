from enum import StrEnum

class ImportPreviewDiagnosticClass(StrEnum):
    ACTIONABLE = "actionable"
    BLOCKING = "blocking"
    INFORMATIONAL = "informational"

    def __str__(self) -> str:
        return str(self.value)
