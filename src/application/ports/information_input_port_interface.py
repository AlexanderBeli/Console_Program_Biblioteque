from abc import ABC, abstractmethod


class BaseInputPort(ABC):
    @abstractmethod
    def type_title(self) -> str: ...

    @abstractmethod
    def type_author(self) -> str: ...

    @abstractmethod
    def type_year(self) -> str: ...

    # для поиска
    @abstractmethod
    def type_id(self) -> str: ...
