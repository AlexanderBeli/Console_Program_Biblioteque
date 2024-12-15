from src.infrastructure.repository.json_data_file_operations import JsonDataFile
from src.application.ports.information_input_port import InformationInputPort
from src.application.ports.number_input_port import CliNumberInputPort
from src.config.messages import MESSAGES
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SearchBooks:

    def __init__(self, input_port: InformationInputPort):
        self.input_port = input_port

    def search_menu(self):
        search_request = CliNumberInputPort().type_number_search_menu()

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
            logging.info(
                f"{MESSAGES["id"]}: {result}\n\
                    {MESSAGES["title"]}: {results[result]["title"]}\n\
                    {MESSAGES["author"]}: {results[result]["author"]}\n\
                    {MESSAGES["year"]}: {results[result]["year"]}\n\
                    {MESSAGES["status"]}: {results[result]["status"]}\n",
            )

    def searching_by_title(self) -> None:
        searching_title = self.input_port.type_title()
        self.searching_engine(searching_title, "title")

    def searching_by_author(self) -> None:
        searching_author = self.input_port.type_author()
        self.searching_engine(searching_author, "author")

    def searching_by_year(self) -> None:
        searching_year = self.input_port.type_year()
        self.searching_engine(searching_year, "year")

    def searching_engine(self, word: str, category: str) -> None:
        books: dict = JsonDataFile().open_biblioteque()
        results = {}

        for book in books:
            if word == books[book][category]:
                results[book] = books[book]

        if len(results) != 0:
            self.show_search_results(results)
        else:
            raise ValueError(MESSAGES["book_not_found_error"])
