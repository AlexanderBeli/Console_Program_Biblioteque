from src.messages import MESSAGES


class BookStatus:
    def default_status(self) -> str:
        return MESSAGES["status_default"]

    def no_available_status(self) -> str:
        return MESSAGES["status_no_available"]
