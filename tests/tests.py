import unittest
from unittest.mock import Mock, patch

from main import BibliotequeController


class TestBibliotequeController(unittest.TestCase):
    def setUp(self):
        self.action = BibliotequeController()
        self.book_data = {
            "title": "Белый вождь",
            "author": "Томас Майн Рид",
            "year": 2017,
            "status": "в наличии",
        }
        self.title = "Белый вождь"
        self.author = "Томас Майн Рид"
        self.year = 2017
        self.status = "в наличии"

    @patch("builtins.input")
    def test_get_the_book_information(self, mocked_input):
        mocked_input.side_effect = [self.title, self.author, self.year]

        id, data = self.action.get_the_book_information()
        self.assertEqual(data["title"], "Белый вождь")
        self.assertEqual(data["author"], "Томас Майн Рид")
        self.assertEqual(data["year"], 2017)


if __name__ == "__main__":
    unittest.main()
