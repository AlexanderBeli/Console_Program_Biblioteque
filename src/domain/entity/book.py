from dataclasses import dataclass
from src.domain.value_object import book_id, book_status


# Так как ввод будет осуществляться постепенно, проверка должна происходить постепенно,
# соответственно валидация будет происходить на этапе ввода
class Book:

    def __init__(self, author:str, title:str, year:str):
        self.author = author
        self.title = title
        self.year = year
        self.status = self._get_book_default_status()

    def _get_book_default_status(self) -> str:
        return book_status.BookStatus.default_status(self)

    def __str__(self):
        return f"{self.author} {self.title} {self.year} {self.status}"

    def __repr__(self) -> dict:
        return  {"title": self.title, "author": self.author, "year": self.year, "status": self.status}
