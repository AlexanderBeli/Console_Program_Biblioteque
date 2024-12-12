import unittest

from Domain.ValueObject.BookAuthor import BookAuthor
from Domain.ValueObject.BookTitle import BookTitle
from Domain.ValueObject.BookYear import BookYear


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
