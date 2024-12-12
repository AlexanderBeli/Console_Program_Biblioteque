from src.messages import MESSAGES
import os
import json


class DeleteBook:

    __biblioteque_adress: str = ".data/biblioteque.json"

    def open_biblioteque(self) -> dict:
        try:
            with open(
                self._DeleteBook__biblioteque_adress, "r"
            ) as biblioteque_opened_for_reading:
                biblioteque_data = json.load(biblioteque_opened_for_reading)
            return biblioteque_data
        except FileNotFoundError:
            raise FileNotFoundError(MESSAGES["file_not_found_error"])

    def add_to_biblioteque(self, data: dict) -> None:
        with open(
            self._DeleteBook__biblioteque_adress, "w"
        ) as biblioteque_opened_for_writing:
            json.dump(data, biblioteque_opened_for_writing)

    def delete_the_book(self) -> None:
        print(MESSAGES["delete_book_info"])
        question = input(MESSAGES["delete_book_confirmation"])
        if int(question) == 1:
            biblioteque_data = self.open_biblioteque()
            book_id = input(MESSAGES["type_book_ID"])
            if book_id in tuple(biblioteque_data.keys()):
                biblioteque_data.pop(book_id)
                self.add_to_biblioteque(biblioteque_data)
            else:
                raise ValueError(MESSAGES["book_not_found_error"])
