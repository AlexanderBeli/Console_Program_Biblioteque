import unittest

from src.domain.entity.book_author import BookAuthor
from src.domain.value_object.book_title import BookTitle
from src.domain.value_object.book_year import BookYear


class TestValueObject(unittest.TestCase):
    def test_book_author_correct_information(self):
        author = BookAuthor("Жюль Верн").validation()
        self.assertEqual(author, "Жюль Верн")

    def test_book_title_correct_information(self):
        title = BookTitle("Путешествие вокруг Света").validation()
        self.assertEqual(title, "Путешествие вокруг Света")

    def test_book_year_correct_information(self):
        year = BookYear("1998").validation()
        self.assertEqual(year, "1998")
