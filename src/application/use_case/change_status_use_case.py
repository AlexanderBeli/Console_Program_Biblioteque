from venv import logger

from src.application.ports.information_input_port import InformationInputPort
from src.application.ports.number_input_port import CliNumberInputPort
from src.config.messages import MESSAGES

from src.infrastructure.repository.json_data_file_operations import JsonDataFile

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChangeStatus:

    def execute(self) -> None:
        change_status = CliNumberInputPort()
        change_book_choice = change_status.type_number_prove_change()

        if change_book_choice == "1":
            biblioteque = JsonDataFile()
            biblioteque_data = biblioteque.open_biblioteque()
            book_id = InformationInputPort().type_id()
            if book_id in tuple(biblioteque_data.keys()):
                logging.info(
                    f"{MESSAGES["status"]}: {biblioteque_data[book_id]["status"]}\n",
                )
                status = change_status.type_number_change_status()
                if status == "1":
                    biblioteque_data[book_id]["status"] = MESSAGES["status_default"]
                elif status == "2":
                    biblioteque_data[book_id]["status"] = MESSAGES[
                        "status_no_available"
                    ]
                else:
                    raise ValueError(MESSAGES["command_not_exist"])
            else:
                raise ValueError(MESSAGES["id_not_exist"])

            biblioteque.add_to_biblioteque(biblioteque_data)

