from src.domain.value_object.book_id import BookId
from src.domain.entity.book import Book

class Library:

    def get_book_id(self) -> str:
        return BookId.get_book_id(self)

    def get_data_from_Book(self, book: Book) -> dict:
        data = book.__repr__()
        return data