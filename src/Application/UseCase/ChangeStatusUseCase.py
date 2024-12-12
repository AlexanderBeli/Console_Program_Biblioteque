from messages import MESSAGES
import os
import json


class ChangeStatus:

    __biblioteque_adress: str = ".data/biblioteque.json"

    def open_biblioteque(self) -> dict:
        try:
            with open(
                self._ChangeStatus__biblioteque_adress, "r"
            ) as biblioteque_opened_for_reading:
                biblioteque_data = json.load(biblioteque_opened_for_reading)
            return biblioteque_data
        except FileNotFoundError:
            raise FileNotFoundError(MESSAGES["file_not_found_error"])

    def add_to_biblioteque(self, data: dict) -> None:
        with open(
            self._ChangeStatus__biblioteque_adress, "w"
        ) as biblioteque_opened_for_writing:
            json.dump(data, biblioteque_opened_for_writing)

    def change_status(self) -> None:
        print(MESSAGES["change_book_info"])
        question = input(MESSAGES["change_book_confirmation"])
        if int(question) == 1:
            biblioteque_data = self.open_biblioteque()
            book_id = input(MESSAGES["type_book_ID"])
            if book_id in tuple(biblioteque_data.keys()):
                print(
                    f"{MESSAGES["status"]}: {biblioteque_data[book_id]["status"]}\n",
                )
                status = input(MESSAGES["status_info"])
                if int(status) == 1:
                    biblioteque_data[book_id]["status"] = MESSAGES["status_default"]
                elif int(status) == 2:
                    biblioteque_data[book_id]["status"] = MESSAGES[
                        "status_no_available"
                    ]
                else:
                    raise ValueError(MESSAGES["command_not_exist"])
            else:
                raise ValueError(MESSAGES["id_not_exist"])

            self.add_to_biblioteque(biblioteque_data)
