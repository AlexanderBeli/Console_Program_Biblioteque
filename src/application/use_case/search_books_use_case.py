from src.config.messages import MESSAGES
import json


class SearchBooks:

    __biblioteque_adress: str = ".data/biblioteque.json"

    def open_biblioteque(self) -> dict:
        try:
            with open(
                self._SearchBooks__biblioteque_adress, "r"
            ) as biblioteque_opened_for_reading:
                biblioteque_data = json.load(biblioteque_opened_for_reading)
            return biblioteque_data
        except FileNotFoundError:
            raise FileNotFoundError(MESSAGES["file_not_found_error"])

    def add_to_biblioteque(self, data: dict) -> None:
        with open(
            self._SearchBooks__biblioteque_adress, "w"
        ) as biblioteque_opened_for_writing:
            json.dump(data, biblioteque_opened_for_writing)

    def search_menu(self):
        search_request = input(MESSAGES["search_menu"])
        #     self.search_menu_action(search_request)

        # def search_menu_action(self, search_request: str):
        if search_request == "1":
            self.searching_by_title()

        elif search_request == "2":
            self.searching_by_author()

        elif search_request == "3":
            self.searching_by_year()
        else:
            raise ValueError(MESSAGES["command_not_exist"])

    def show_search_results(self, results: dict) -> None:
        for result in results:
            print(
                f"{MESSAGES["id"]}: {result}\n\
                    {MESSAGES["title"]}: {results[result]["title"]}\n\
                    {MESSAGES["author"]}: {results[result]["author"]}\n\
                    {MESSAGES["year"]}: {results[result]["year"]}\n\
                    {MESSAGES["status"]}: {results[result]["status"]}\n",
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
        books: dict = self.open_biblioteque()
        results = {}
        for book in books:
            if word == books[book][category]:
                results[book] = books[book]
            else:
                raise ValueError(MESSAGES["book_not_found_error"])
        if len(results) != 0:
            self.show_search_results(results)
        else:
            raise ValueError(MESSAGES["book_not_found_error"])
