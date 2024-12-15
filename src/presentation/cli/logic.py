from src.application.ports.information_input_port import InformationInputPort
from src.application.ports.number_input_port import CliNumberInputPort

from src.config.messages import MESSAGES
from src.application.use_case.create_book_use_case import CreateBookUseCase
from src.application.use_case.delete_book_use_case import DeleteBookUseCase
from src.application.use_case.search_books_use_case import SearchBooks
from src.application.use_case.list_books_use_case import ListBooks
from src.application.use_case.change_status_use_case import ChangeStatus
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run() -> None:
    while True:
        action = InformationInputPort()
        try:
            choice = CliNumberInputPort().type_number_start_menu().strip()
            if not choice:
                raise ValueError(MESSAGES["command_not_exist"])
            match choice:
                case "1":
                    CreateBookUseCase(action).execute()
                case "2":
                    DeleteBookUseCase().execute()
                case "3":
                    SearchBooks(action).search_menu()
                case "4":
                    ListBooks().execute()
                case "5":
                    ChangeStatus().execute()
                case "6":
                    logging.info(MESSAGES["exit_message"])
                    break
                case _:
                    logging.error(MESSAGES["command_not_exist"])
        except ValueError as err:
            raise ValueError(MESSAGES["mistake"] + ":\n" + err)
