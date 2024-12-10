from src.controlers import BibliotequeController
from src.messages import MESSAGES


def main() -> None:
    while True:
        action = BibliotequeController()
        main_request = action.main_menu()

        if int(main_request) == 1:
            action.add_book_controller()

        elif int(main_request) == 2:
            action.delete_the_book()

        elif int(main_request) == 3:
            search_request = action.search_menu()
            if int(search_request) == 1:
                action.searching_by_title()

            elif int(search_request) == 2:
                action.searching_by_author()

            elif int(search_request) == 3:
                action.searching_by_year()

        elif int(main_request) == 4:
            action.list_books()

        elif int(main_request) == 5:
            action.change_status()

        elif int(main_request) == 6:
            print(MESSAGES["exit_message"])
            break

        else:
            print(MESSAGES["command_not_exist"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(MESSAGES["exit_message"])
