from Domain.Repository.InformationInputPortInterface import (
    InformationInputPortInterface,
)
from Domain.ValueObject.BookTitle import BookTitle
from Domain.ValueObject.BookAuthor import BookAuthor
from Domain.ValueObject.BookYear import BookYear
from Domain.ValueObject.BookId import BookId
from messages import MESSAGES


class CliInformationInputPort(InformationInputPortInterface):

    def type_title(self) -> str:
        cli_title = input(MESSAGES["add_book_title"])
        book_title_validation = BookTitle(cli_title).validation()
        return book_title_validation

    def type_author(self) -> str:
        cli_author = input(MESSAGES["add_book_author"])
        book_author_validation = BookAuthor(cli_author).validation()
        return book_author_validation

    def type_year(self) -> str:
        cli_year = input(MESSAGES["add_book_year"])
        book_year_validation = BookYear(cli_year).validation()
        return book_year_validation

    # для режима поиска
    def type_id(self) -> str:
        cli_id = input(MESSAGES["type_book_ID"])
        book_id_validation = BookId().validation(cli_id)
        return book_id_validation
