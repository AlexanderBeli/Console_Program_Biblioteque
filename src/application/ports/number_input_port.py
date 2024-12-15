from src.application.ports.number_input_port_interface import NumberInputPortInterface
from src.config.messages import MESSAGES


class CliNumberInputPort(NumberInputPortInterface):

    def type_number_start_menu(self) -> str:
        cli_type_number_start_menu = input(MESSAGES["start_menu"])
        checked_cli_type_number_start_menu = self.type_number_validation(self, cli_type_number_start_menu)
        return checked_cli_type_number_start_menu

    def type_number_search_menu(self) -> str:
        cli_type_number_search_menu = input(MESSAGES["search_menu"])
        checked_cli_type_number_search_menu = self.type_number_validation(self, cli_type_number_search_menu)
        return checked_cli_type_number_search_menu

    def type_number_prove_delete(self) -> str:
        print(MESSAGES["delete_book_info"])
        cli_type_number_question = input(MESSAGES["delete_book_confirmation"])
        checked_cli_type_number_question = self.type_number_validation(self, cli_type_number_question)
        return checked_cli_type_number_question

    def type_number_prove_change(self) -> str:
        print(MESSAGES["change_book_info"])
        cli_type_number_question = input(MESSAGES["change_book_confirmation"])
        checked_cli_type_number_question = self.type_number_validation(self, cli_type_number_question)
        return checked_cli_type_number_question

    def type_number_change_status(self) -> str:
        cli_type_number_question = input(MESSAGES["status_info"])
        checked_cli_type_number_question = self.type_number_validation(self, cli_type_number_question)
        return checked_cli_type_number_question

    @staticmethod
    def type_number_validation(self, typed_number):
        try:
            int_typed_number = int(typed_number)
            return typed_number
        except ValueError:
            raise ValueError(MESSAGES["command_not_exist"])
