from Domain.Entity.Book import Book
from Infrastructure.Repository.InformationInputRepository import CliInformationInputPort
from messages import MESSAGES
import os
import json


class CreateBook:

    __biblioteque_adress: str = ".data/biblioteque.json"

    def open_biblioteque(self) -> dict:
        try:
            with open(
                self._CreateBook__biblioteque_adress, "r"
            ) as biblioteque_opened_for_reading:
                biblioteque_data = json.load(biblioteque_opened_for_reading)
            return biblioteque_data
        except FileNotFoundError:
            raise FileNotFoundError(MESSAGES["file_not_found_error"])

    def add_to_biblioteque(self, data: dict) -> None:
        with open(
            self._CreateBook__biblioteque_adress, "w"
        ) as biblioteque_opened_for_writing:
            json.dump(data, biblioteque_opened_for_writing)

    def create_book() -> tuple[str, dict[str, str]]:
        action = CliInformationInputPort()

        book_title = action.type_title()
        book_author = action.type_author()
        book_year = action.type_year()

        book = Book(book_author, book_title, book_year)
        book_id = Book.get_book_id()
        book_status = Book.get_book_default_status()

        data = {
            "title": book_title,
            "author": book_author,
            "year": book_year,
            "status": book_status,
        }

        return book_id, data

    def add_book_controller(self) -> None:
        book_id, data = self.create_book()
        if not os.path.exists(self._CreateBook__biblioteque_adress):
            data_for_dumping = {book_id: data}
            self.add_to_biblioteque(data_for_dumping)
        else:
            biblioteque_data = self.open_biblioteque()
            biblioteque_data[book_id] = data
            self.add_to_biblioteque(biblioteque_data)
