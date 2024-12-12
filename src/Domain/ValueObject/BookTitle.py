from dataclasses import dataclass

from Domain.Validation import BookValidation
from Domain.ValueObject.AbstractInputOutput import InputOutput


@dataclass
class BookTitle(InputOutput):
    title: str

    def validation(self) -> str:
        checking = BookValidation.BookValidation(self.title)
        return checking.book_title_validation()
