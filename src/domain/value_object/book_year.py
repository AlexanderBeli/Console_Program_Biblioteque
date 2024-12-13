from dataclasses import dataclass

from src.application.ports.abstract_input_output import InputOutput
from src.domain.service.book_validation import BookValidation


@dataclass
class BookYear(InputOutput):
    year: str

    def validation(self) -> str:
        checking = BookValidation(self.year)
        return checking.book_year_validation()
