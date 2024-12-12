from dataclasses import dataclass

from src.Domain.Validation import BookValidation
from src.Domain.ValueObject.AbstractInputOutput import InputOutput


@dataclass
class BookYear(InputOutput):
    year: str

    def validation(self) -> str:
        checking = BookValidation.BookValidation(self.year)
        return checking.book_year_validation()
