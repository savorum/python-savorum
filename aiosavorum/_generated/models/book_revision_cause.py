from enum import StrEnum

class BookRevisionCause(StrEnum):
    API = "api"
    MANUAL_EDIT = "manual_edit"
    RECIPE_LIFECYCLE = "recipe_lifecycle"
    RESTORE = "restore"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
