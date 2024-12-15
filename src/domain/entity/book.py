from dataclasses import dataclass, field
from src.domain.value_object import book_id, book_status


# Так как ввод будет осуществляться постепенно, проверка должна происходить постепенно,
# соответственно валидация будет происходить на этапе ввода
@dataclass
class Book:
    author: str
    title: str
    year: str
    status: str = field(init=False)

    def __post_init__(self) -> None:
        self.status = book_status.BookStatus.default_status(self)
