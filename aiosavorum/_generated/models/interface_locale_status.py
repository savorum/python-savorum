from enum import StrEnum

class InterfaceLocaleStatus(StrEnum):
    PREVIEW = "preview"
    SUPPORTED = "supported"

    def __str__(self) -> str:
        return str(self.value)
