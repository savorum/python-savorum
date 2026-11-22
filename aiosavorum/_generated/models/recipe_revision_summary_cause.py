from enum import StrEnum

class RecipeRevisionSummaryCause(StrEnum):
    API = "api"
    IMPORT = "import"
    MANUAL_EDIT = "manual_edit"
    RESTORE = "restore"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
