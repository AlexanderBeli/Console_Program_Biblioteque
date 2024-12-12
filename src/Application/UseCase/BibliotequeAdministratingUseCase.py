from src.Infrastructure.Repository.InformationInputRepository import CliInformationInputPort
from src.Infrastructure.Repository.NumberInputRepository import CliNumberInputPort

from src.messages import MESSAGES
from src.Application.UseCase.CreateBookUseCase import CreateBook
from src.Application.UseCase.DeleteBookUseCase import DeleteBook
from src.Application.UseCase.SearchBooksUseCase import SearchBooks
from src.Application.UseCase.ListBooksUseCase import ListBooks
from src.Application.UseCase.ChangeStatusUseCase import ChangeStatus


class CreateBookUseCase:
    pass


def run() -> None:
    while True:
        action = CliInformationInputPort()
        try:
            choice = CliNumberInputPort().type_number_start_menu().strip()
            if not choice:
                raise ValueError(MESSAGES["command_not_exist"])
            match choice:
                case "1":
                    CreateBook().add_book_controller()
                case "2":
                    DeleteBook().delete_the_book()
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
