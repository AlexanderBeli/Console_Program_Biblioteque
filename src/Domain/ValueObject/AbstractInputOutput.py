from abc import ABC, abstractmethod


class InputOutput(ABC):

    @abstractmethod
    def validation(self) -> str: ...
