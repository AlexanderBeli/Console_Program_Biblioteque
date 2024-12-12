from dataclasses import dataclass

from Domain.Validation import BookValidation
from Domain.ValueObject.AbstractInputOutput import InputOutput


@dataclass
class BookAuthor(InputOutput):
    author: str

    def validation(self) -> str:
        checking = BookValidation.BookValidation(self.author)
        return checking.book_author_validation()
