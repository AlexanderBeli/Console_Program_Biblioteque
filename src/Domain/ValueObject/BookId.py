import uuid
from src.Domain.Validation import BookValidation


class BookId:

    def get_book_id(self) -> str:
        return str(uuid.uuid4())

    # Для проверки в режиме поиска
    def validation(self, typed_uuid):
        checking = BookValidation.BookValidation(typed_uuid)
        return checking.uuid_validation()
