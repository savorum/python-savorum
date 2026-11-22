from enum import StrEnum

class SavedViewSort(StrEnum):
    ACTIVE_TIME_ASC = "active-time-asc"
    COOKED_ASC = "cooked-asc"
    COOKED_DESC = "cooked-desc"
    CREATED_DESC = "created-desc"
    RANDOM = "random"
    RATING_DESC = "rating-desc"
    RELEVANCE = "relevance"
    TIMES_COOKED_DESC = "times-cooked-desc"
    TITLE_ASC = "title-asc"
    TOTAL_TIME_ASC = "total-time-asc"
    UPDATED_DESC = "updated-desc"

    def __str__(self) -> str:
        return str(self.value)
