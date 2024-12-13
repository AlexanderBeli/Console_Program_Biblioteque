from dataclasses import dataclass

from src.domain.service.book_validation import BookValidation
from src.application.ports.abstract_input_output import InputOutput


@dataclass
class BookAuthor(InputOutput):
    author: str

    def validation(self) -> str:
        checking = BookValidation(self.author)
        return checking.book_author_validation()
