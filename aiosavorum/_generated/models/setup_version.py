from enum import IntEnum

class SetupVersion(IntEnum):
    VALUE_1 = 1

    def __str__(self) -> str:
        return str(self.value)
