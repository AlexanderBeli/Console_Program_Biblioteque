import unittest
from dataclasses import asdict
from unittest import mock

from src.application.ports.information_input_port import InformationInputPort
from src.application.use_case.create_book_use_case import CreateBookUseCase
from src.domain.entity.book import Book
from src.infrastructure.repository.json_data_file_operations import JsonDataFile
from src.infrastructure.repository.library_extra_operations import Library


class TestCreateBookUseCase(unittest.TestCase):

    def setUp(self):
        # self.mock_storage = MagicMock(spec=JsonDataFile)
        # self.action = CreateBookUseCase(InformationInputPort()).execute()
        self.book_data = {
            "title": "Белый вождь",
            "author": "Томас Майн Рид",
            "year": 2017,
            "status": "в наличии",
        }
        self.title = "Белый вождь"
        self.author = "Томас Майн Рид"
        self.year = 2017
        # self.status = "в наличии"

    def test_create_book(self):
        book = Book(self.title, self.author, self.year)
        book_dict = asdict(book)
        self.assertEqual(book_dict["status"], "в наличии")

    @mock.patch("os.path.exists", return_value=False)
    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_add_to_dict_no_file(self, mock_file, mock_file_exists):
        JsonDataFile().add_book_controller(book_id="1234", data=self.book_data)
        mock_file_exists.assert_called_once_with(".data/biblioteque.json")
        mock_file.assert_called_once_with(".data/biblioteque.json", "w")

    @mock.patch("json.dump")
    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="{}")
    def test_add_to_dict_has_file(
        self,
        mock_file_open: mock.MagicMock,
        mock_file_exists: mock.MagicMock,
        mock_jsondump: mock.MagicMock,
    ):
        JsonDataFile().add_book_controller(book_id="1234", data=self.book_data)
        mock_file_exists.assert_called_once_with(".data/biblioteque.json")
        self.assertEqual(
            [
                mock.call(".data/biblioteque.json", "r"),
                mock.call(".data/biblioteque.json", "w"),
            ],
            mock_file_open.call_args_list,
        )
        expected_data = {"1234": self.book_data}
        mock_jsondump.assert_called_once_with(expected_data, mock.ANY)

    # @patch("builtins.open", new_callable=mock_open)
    # def test_add_to_dict(self, mock_file):
    #     JsonDataFile().add_book_controller(book_id="1234", data=self.book_data)

    # def test_add_book(self):
    # self.mock_storage.open_biblioteque.return_value = []
    # book = Book("Book 1", "Author 1", "2000")
    # book_dict = asdict(book)
    # self.mock_storage.add_to_biblioteque({book_dict}).assert_called_once()
    # self.assertEqual(self.mock_storage.add_to_biblioteque.call_args[0][0], [book_dict.__dict__])

    # @patch("builtins.input")
    # def test_add_the_book_information(self, mocked_input):
    #     mocked_input.side_effect = [self.title, self.author, self.year]
    #
    #     self.assertEqual(book_data["title"], "Белый вождь")
    #     self.assertEqual(book_data["author"], "Томас Майн Рид")
    #     self.assertEqual(book_data["year"], 2017)


if __name__ == "__main__":
    unittest.main()
