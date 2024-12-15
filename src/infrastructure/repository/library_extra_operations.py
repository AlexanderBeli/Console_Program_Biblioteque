from src.domain.value_object.book_id import BookId

class Library:

    def get_book_id(self) -> str:
        return BookId.get_book_id(self)