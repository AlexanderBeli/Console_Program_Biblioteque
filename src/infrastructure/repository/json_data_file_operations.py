from src.config.messages import MESSAGES
import json
import os

class JsonDataFile:
    __biblioteque_adress: str = ".data/biblioteque.json"

    def open_biblioteque(self) -> dict:
        try:
            with open(
                    self._JsonDataFile__biblioteque_adress, "r"
            ) as biblioteque_opened_for_reading:
                biblioteque_data = json.load(biblioteque_opened_for_reading)
            return biblioteque_data
        except FileNotFoundError:
            raise FileNotFoundError(MESSAGES["file_not_found_error"])


    def add_to_biblioteque(self, data: dict) -> None:
        with open(
                self._JsonDataFile__biblioteque_adress, "w"
        ) as biblioteque_opened_for_writing:
            json.dump(data, biblioteque_opened_for_writing)

    def add_book_controller(self, book_id, data) -> None:
        if not os.path.exists(self._JsonDataFile__biblioteque_adress):
            data_for_dumping = {book_id: data}
            self.add_to_biblioteque(data_for_dumping)
        else:
            biblioteque_data = self.open_biblioteque()
            biblioteque_data[book_id] = data
            self.add_to_biblioteque(biblioteque_data)