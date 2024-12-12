from Domain.Repository.NumberInputPortInterface import NumberInputPortInterface
from messages import MESSAGES


class CliNumberInputPort(NumberInputPortInterface):

    def type_number_start_menu(self) -> str:
        cli_type_number_start_menu = input(MESSAGES["start_menu"])
        checked_cli_type_number_start_menu = self.type_number_validation(
            cli_type_number_start_menu
        )
        return checked_cli_type_number_start_menu

    def type_number_search_menu(self) -> str:
        cli_type_number_search_menu = input(MESSAGES["search_menu"])
        checked_cli_type_number_search_menu = self.type_number_validation(
            cli_type_number_search_menu
        )
        return checked_cli_type_number_search_menu

    @staticmethod
    def type_number_validation(self, typed_number):
        try:
            int_typed_number = int(typed_number)
            return typed_number
        except ValueError:
            raise ValueError(MESSAGES["command_not_exist"])
