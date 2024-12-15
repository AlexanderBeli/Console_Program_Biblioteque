from src.infrastructure.repository.json_data_file_operations import JsonDataFile
from src.config.messages import MESSAGES
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ListBooks:

    def execute(self) -> None:
        biblioteque_data: dict = JsonDataFile().open_biblioteque()
        self.show_search_results(biblioteque_data)

    def show_search_results(self, results: dict) -> None:
        for result in results:
            logging.info(
                f"{MESSAGES["id"]}: {result}\n\
                    {MESSAGES["title"]}: {results[result]["title"]}\n\
                    {MESSAGES["author"]}: {results[result]["author"]}\n\
                    {MESSAGES["year"]}: {results[result]["year"]}\n\
                    {MESSAGES["status"]}: {results[result]["status"]}\n",
            )
