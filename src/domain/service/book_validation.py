from dataclasses import dataclass

from src.config.messages import MESSAGES

@dataclass
class BookValidation:
    input_word: str

    _MIN_VALID_PUBLISHED_YEAR: int = 1860
    _MAX_VALID_PUBLISHED_YEAR: int = 2024
    _MIN_VALID_LENGTH_WORD: int = 3
    _MAX_VALID_LENGTH_WORD_TITLE: int = 100
    _MAX_VALID_LENGTH_WORD_AUTHOR: int = 30
    _VALID_LENGTH_YEAR: int = 4
    _VALID_LENGTH_UUID: int = 36


    def _input_word_length(self) -> int:
        return len(self.input_word)

    def book_title_validation(self) -> str:
        input_word_length = self._input_word_length()
        if not (self._MIN_VALID_LENGTH_WORD <= input_word_length <= self._MAX_VALID_LENGTH_WORD_TITLE):
            if input_word_length < self._MIN_VALID_LENGTH_WORD:
                raise ValueError(MESSAGES["book_title_length_less_three_symbols"])
            elif input_word_length > self._MAX_VALID_LENGTH_WORD_TITLE:
                raise ValueError(MESSAGES["book_title_length_more_hundred_symbols"])
        else:
            return self.input_word

    def book_author_validation(self) -> str:
        input_word_length = self._input_word_length()
        if not (self._MIN_VALID_LENGTH_WORD <= input_word_length <= self._MAX_VALID_LENGTH_WORD_AUTHOR):
            if input_word_length < self._MIN_VALID_LENGTH_WORD:
                raise ValueError(MESSAGES["book_author_length_less_three_symbols"])
            elif input_word_length > self._MAX_VALID_LENGTH_WORD_AUTHOR:
                raise ValueError(MESSAGES["book_author_length_more_hundred_symbols"])
        else:
            return self.input_word

    def book_year_validation(self) -> str:
        input_word_length = self._input_word_length()
        if input_word_length != self._VALID_LENGTH_YEAR:
            raise ValueError(MESSAGES["book_year_length_should_be_four_symbols"])
        elif int(self.input_word):
            year = int(self.input_word)
            if year > self._MAX_VALID_PUBLISHED_YEAR:
                raise ValueError(MESSAGES["book_year_after_2024"])
            elif year < self._MIN_VALID_PUBLISHED_YEAR:
                raise ValueError(MESSAGES["book_year_before_1860"])
            else:
                return self.input_word
        else:
            raise ValueError(MESSAGES["book_year_should_be_numbers"])

    def uuid_validation(self) -> str:
        input_word_length = self._input_word_length()
        if input_word_length == self._VALID_LENGTH_UUID:
            return self.input_word
        else:
            raise ValueError(MESSAGES["uuid_length"])
