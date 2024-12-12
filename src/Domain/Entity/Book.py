from dataclasses import dataclass
from ValueObject import BookAuthor, BookId, BookTitle, BookYear, BookStatus


# Так как ввод будет осуществляться постепенно, проверка должна происходить постепенно,
# соответственно валидация будет происходить на этапе ввода
@dataclass
class Book:
    author: str
    title: str
    year: str

    def get_book_id(self) -> str:
        return BookId.BookId.get_book_id()

    def get_book_default_status(self) -> str:
        return BookStatus.BookStatus.default_status()
