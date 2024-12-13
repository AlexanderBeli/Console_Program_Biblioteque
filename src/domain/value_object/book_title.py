from dataclasses import dataclass

from src.domain.service.book_validation import BookValidation
from src.application.ports.abstract_input_output import InputOutput


@dataclass
class BookTitle(InputOutput):
    title: str

    def validation(self) -> str:
        checking = BookValidation(self.title)
        return checking.book_title_validation()