from src.application.ports.information_input_port import InformationInputPort
from src.application.ports.number_input_port import CliNumberInputPort
from src.config.messages import MESSAGES

from src.infrastructure.repository.json_data_file_operations import JsonDataFile


class DeleteBookUseCase:

    def execute(self) -> None:
        delete_book_choice = CliNumberInputPort().type_number_prove_delete()

        if delete_book_choice == "1":
            biblioteque = JsonDataFile()
            biblioteque_data = biblioteque.open_biblioteque()
            book_id = InformationInputPort().type_id()
            if book_id in tuple(biblioteque_data.keys()):
                biblioteque_data.pop(book_id)
                biblioteque.add_to_biblioteque(biblioteque_data)
            else:
                raise ValueError(MESSAGES["book_not_found_error"])


