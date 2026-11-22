from enum import StrEnum

class CommitAutomationImportRequestPolicy(StrEnum):
    ALLOW_WARNINGS = "allow-warnings"
    REQUIRE_NO_WARNINGS = "require-no-warnings"

    def __str__(self) -> str:
        return str(self.value)
