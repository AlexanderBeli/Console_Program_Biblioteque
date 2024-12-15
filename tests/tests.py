import unittest
from unittest.mock import Mock, patch, MagicMock, mock_open
from dataclasses import asdict

from src.application.use_case.create_book_use_case import CreateBookUseCase
from src.application.ports.information_input_port import InformationInputPort
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
