from enum import StrEnum

class ImportJobDiagnosticSummaryClass(StrEnum):
    ACTIONABLE = "actionable"
    BLOCKING = "blocking"
    INFORMATIONAL = "informational"

    def __str__(self) -> str:
        return str(self.value)
