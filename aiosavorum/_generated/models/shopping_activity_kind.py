from enum import StrEnum

class ShoppingActivityKind(StrEnum):
    ADD = "add"
    BOUGHT = "bought"
    CREATE_LIST = "create-list"
    EDIT = "edit"
    MERGE = "merge"
    MOVE = "move"
    REMOVE = "remove"
    RENAME_LIST = "rename-list"
    REOPENED = "reopened"
    RESTORE = "restore"
    REVIEW = "review"
    SPLIT = "split"

    def __str__(self) -> str:
        return str(self.value)
