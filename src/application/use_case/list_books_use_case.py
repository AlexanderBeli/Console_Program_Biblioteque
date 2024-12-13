from src.config.messages import MESSAGES
import os
import json


class ListBooks:

    __biblioteque_adress: str = ".data/biblioteque.json"

    def open_biblioteque(self) -> dict:
        try:
            with open(
                self._ListBooks__biblioteque_adress, "r"
            ) as biblioteque_opened_for_reading:
                biblioteque_data = json.load(biblioteque_opened_for_reading)
            return biblioteque_data
        except FileNotFoundError:
            raise FileNotFoundError(MESSAGES["file_not_found_error"])

    def list_books(self) -> None:
        if os.path.exists(self._ListBooks__biblioteque_adress):
            biblioteque_data = self.open_biblioteque()
            self.show_search_results(biblioteque_data)
        else:
            raise FileNotFoundError(MESSAGES["file_not_found_error"])

    def show_search_results(self, results: dict) -> None:
        for result in results:
            print(
                f"{MESSAGES["id"]}: {result}\n\
                    {MESSAGES["title"]}: {results[result]["title"]}\n\
                    {MESSAGES["author"]}: {results[result]["author"]}\n\
                    {MESSAGES["year"]}: {results[result]["year"]}\n\
                    {MESSAGES["status"]}: {results[result]["status"]}\n",
            )
