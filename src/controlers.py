import json
import os.path
import uuid

from src.messages import MESSAGES


class BibliotequeController:

    __biblioteque_adress = ".data/biblioteque.json"

    def open_biblioteque(self) -> dict:
        try:
            with open(
                self._BibliotequeController__biblioteque_adress, "r"
            ) as biblioteque_opened_for_reading:
                biblioteque_data = json.load(biblioteque_opened_for_reading)
            return biblioteque_data
        except FileNotFoundError:
            print(MESSAGES["file_not_found_error"])

    def add_to_biblioteque(self, data: dict) -> None:
        with open(
            self._BibliotequeController__biblioteque_adress, "w"
        ) as biblioteque_opened_for_writing:
            json.dump(data, biblioteque_opened_for_writing)

    def main_menu(self) -> str:
        return input(MESSAGES["start_menu"])

    def search_menu(self) -> str:
        return input(MESSAGES["search_menu"])

    def show_search_results(self, results: dict) -> None:
        for result in results:
            print(
                f"{MESSAGES["id"]}: {result}\n\
                    {MESSAGES["title"]}: {results[result]["title"]}\n\
                    {MESSAGES["author"]}: {results[result]["author"]}\n\
                    {MESSAGES["year"]}: {results[result]["year"]}\n\
                    {MESSAGES["status"]}: {results[result]["status"]}\n"
            )

    def searching_by_title(self) -> None:
        searching_title = input(MESSAGES["searching_title"])
        self.searching_engine(searching_title, "title")

    def searching_by_author(self) -> None:
        searching_author = input(MESSAGES["searching_author"])
        self.searching_engine(searching_author, "author")

    def searching_by_year(self) -> None:
        searching_year = input(MESSAGES["searching_year"])
        self.searching_engine(searching_year, "year")

    def searching_engine(self, word: str, category: str) -> None:
        books = self.open_biblioteque()
        results = {}
        for book in books:
            if word == books[book][category]:
                results[book] = books[book]
            else:
                return MESSAGES["book_not_found_error"]
        if len(results) != 0:
            self.show_search_results(results)
        else:
            return MESSAGES["book_not_found_error"]

    def input_main_book_info(self) -> tuple[str, str, str, str]:
        title = input(MESSAGES["add_book_title"])
        author = input(MESSAGES["add_book_author"])
        year = input(MESSAGES["add_book_year"])
        status = MESSAGES["status_default"]
        return title, author, year, status

    def add_book_controller(self) -> None:
        id, data = self.get_the_book_information()
        if not os.path.exists(self._BibliotequeController__biblioteque_adress):
            data_for_dumping = {id: data}
            self.add_to_biblioteque(data_for_dumping)
        else:
            biblioteque_data = self.open_biblioteque()
            biblioteque_data[id] = data
            self.add_to_biblioteque(biblioteque_data)

    def get_the_book_information(self) -> tuple[str, dict[str, str]]:
        title, author, year, status = self.input_main_book_info()
        id = str(uuid.uuid4())
        data = {
            "title": title,
            "author": author,
            "year": year,
            "status": status,
        }
        return id, data

    def list_books(self) -> None:
        if os.path.exists(self._BibliotequeController__biblioteque_adress):
            biblioteque_data = self.open_biblioteque()
            self.show_search_results(biblioteque_data)
        else:
            print(MESSAGES["file_not_found_error"])

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
                return MESSAGES["book_not_found_error"]

    def change_status(self) -> None:
        print(MESSAGES["change_book_info"])
        question = input(MESSAGES["change_book_confirmation"])
        if int(question) == 1:
            biblioteque_data = self.open_biblioteque()
            book_id = input(MESSAGES["type_book_ID"])
            if book_id in tuple(biblioteque_data.keys()):
                print(f"{MESSAGES["status"]}: {biblioteque_data[book_id]["status"]}\n")
                status = input(MESSAGES["status_info"])
                if int(status) == 1:
                    biblioteque_data[book_id]["status"] = MESSAGES["status_default"]
                elif int(status) == 2:
                    biblioteque_data[book_id]["status"] = MESSAGES[
                        "status_no_available"
                    ]
                else:
                    print(MESSAGES["command_not_exist"])
            else:
                print(MESSAGES["id_not_exist"])

                self.add_to_biblioteque(biblioteque_data)
