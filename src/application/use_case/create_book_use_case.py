from src.domain.entity.book import Book
from src.application.ports.information_input_port import InformationInputPort

from dataclasses import asdict

from src.infrastructure.repository.json_data_file_operations import JsonDataFile
from src.infrastructure.repository.library_extra_operations import Library


class CreateBookUseCase:

    def __init__(self, input_port: InformationInputPort):
        self.input_port = input_port

    def execute(self) -> None:

        book_title = self.input_port.type_title()
        book_author = self.input_port.type_author()
        book_year = self.input_port.type_year()

        book = Book(book_author, book_title, book_year)

        book_data = asdict(book)
        open_library = Library()
        book_id = open_library.get_book_id()
        save_book_data = JsonDataFile().add_book_controller(book_id, book_data)

