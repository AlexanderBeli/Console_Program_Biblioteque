from dataclasses import dataclass

from src.Domain.Validation import BookValidation
from src.Domain.ValueObject.AbstractInputOutput import InputOutput


@dataclass
class BookAuthor(InputOutput):
    author: str

    def validation(self) -> str:
        checking = BookValidation.BookValidation(self.author)
        return checking.book_author_validation()
