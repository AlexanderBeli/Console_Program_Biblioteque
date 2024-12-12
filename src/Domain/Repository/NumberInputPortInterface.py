from abc import ABC, abstractmethod


class NumberInputPortInterface(ABC):
    @abstractmethod
    def type_number(self) -> str: ...
