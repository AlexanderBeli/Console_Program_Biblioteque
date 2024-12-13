from abc import ABC, abstractmethod


class NumberInputPortInterface(ABC):
    @abstractmethod
    def type_number_start_menu(self) -> str: ...

    @abstractmethod
    def type_number_search_menu(self) -> str: ...
