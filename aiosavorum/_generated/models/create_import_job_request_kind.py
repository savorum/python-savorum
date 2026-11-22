from enum import StrEnum

class CreateImportJobRequestKind(StrEnum):
    FILE = "file"
    TEXT = "text"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
