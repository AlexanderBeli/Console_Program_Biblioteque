from src.application.ports.information_input_port import InformationInputPort
from src.application.ports.number_input_port import CliNumberInputPort

from src.config.messages import MESSAGES
from src.application.use_case.create_book_use_case import CreateBookUseCase
from src.application.use_case.delete_book_use_case import DeleteBookUseCase
from src.application.use_case.search_books_use_case import SearchBooks
from src.application.use_case.list_books_use_case import ListBooks
from src.application.use_case.change_status_use_case import ChangeStatus
from src.infrastructure.repository.library_crud_operations import Library
from src.infrastructure.repository.json_data_file_operations import JsonDataFile


def run() -> None:
    while True:
        action = InformationInputPort()
        try:
            choice = CliNumberInputPort().type_number_start_menu().strip()
            if not choice:
                raise ValueError(MESSAGES["command_not_exist"])
            match choice:
                case "1":
                    book = CreateBookUseCase(action).execute()
                    open_library = Library()
                    book_data = open_library.get_data_from_Book(book)
                    book_id = open_library.get_book_id()
                    save_book_data = JsonDataFile().add_book_controller(book_id, book_data)
                case "2":
                    DeleteBookUseCase().delete_the_book()
                case "3":
                    SearchBooks().search_menu()
                case "4":
                    ListBooks().list_books()
                case "5":
                    ChangeStatus().change_status()
                case "6":
                    print(MESSAGES["exit_message"])
                    break
                case _:
                    print(MESSAGES["command_not_exist"])
        except ValueError as err:
            raise ValueError(MESSAGES["mistake"] + ":\n" + err)
