import logging

from src.controlers import BibliotequeController
from src.messages import MESSAGES


def main() -> None:
    while True:
        action = BibliotequeController()

        try:
            choice = action.main_menu().strip()
            if not choice:
                raise ValueError(MESSAGES["command_not_exist"])
            match choice:
                case "1":
                    action.add_book_controller()
                case "2":
                    action.delete_the_book()
                case "3":
                    action.search_menu()
                case "4":
                    action.list_books()
                case "5":
                    action.change_status()
                case "6":
                    print(MESSAGES["exit_message"])
                    break
                case _:
                    print(MESSAGES["command_not_exist"])
        except ValueError as err:
            print(MESSAGES["mistake"] + ":\n" + err)


if __name__ == "__main__":
    try:
        logging.basicConfig()
        main()
    except KeyboardInterrupt:
        print(MESSAGES["exit_message"])
