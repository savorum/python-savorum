from enum import StrEnum

class CreateImportJobRequestPolicy(StrEnum):
    ALLOW_WARNINGS = "allow-warnings"
    PREVIEW_ONLY = "preview-only"
    REQUIRE_NO_WARNINGS = "require-no-warnings"

    def __str__(self) -> str:
        return str(self.value)
