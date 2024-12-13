from src.domain.entity.book import Book
from src.application.ports.information_input_port import InformationInputPort


class CreateBookUseCase:

    def __init__(self, input_port: InformationInputPort):
        self.input_port = input_port

    def execute(self) -> Book:

        book_title = self.input_port.type_title()
        book_author = self.input_port.type_author()
        book_year = self.input_port.type_year()

        book = Book(book_author, book_title, book_year)

        return book

