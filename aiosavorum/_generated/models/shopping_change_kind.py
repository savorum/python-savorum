from enum import StrEnum

class ShoppingChangeKind(StrEnum):
    ADD = "add"
    EDIT = "edit"
    MERGE = "merge"
    MOVE = "move"
    REMOVE = "remove"
    RESTORE = "restore"
    SPLIT = "split"

    def __str__(self) -> str:
        return str(self.value)
