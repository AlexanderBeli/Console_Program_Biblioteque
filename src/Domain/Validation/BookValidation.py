from dataclasses import dataclass

from src.messages import MESSAGES


@dataclass
class BookValidation:
    input_word: str

    def input_word_length(self) -> int:
        return len(self.input_word)

    def book_title_validation(self) -> str:
        input_word_length = self.input_word_length()
        if not (3 <= input_word_length <= 100):
            if input_word_length < 3:
                raise ValueError(MESSAGES["book_title_length_less_three_symbols"])
            elif input_word_length > 100:
                raise ValueError(MESSAGES["book_title_length_more_hundred_symbols"])
            else:
                return self.input_word

    def book_author_validation(self) -> str:
        input_word_length = self.input_word_length()
        if not (3 <= input_word_length <= 30):
            if input_word_length < 3:
                raise ValueError(MESSAGES["book_author_length_less_three_symbols"])
            elif input_word_length > 30:
                raise ValueError(MESSAGES["book_author_length_more_hundred_symbols"])
            else:
                return self.input_word

    def book_year_validation(self) -> str:
        input_word_length = self.input_word_length()
        if input_word_length != 4:
            raise ValueError(MESSAGES["book_year_length_should_be_four_symbols"])
        if int(self.input_word):
            year = int(self.input_word)
            if year > 2024:
                raise ValueError(MESSAGES["book_year_after_2024"])
            elif year < 1860:
                raise ValueError(MESSAGES["book_year_before_1860"])
            else:
                return self.input_word
        else:
            raise ValueError(MESSAGES["book_year_should_be_numbers"])

    def uuid_validation(self) -> str:
        input_word_length = self.input_word_length()
        if input_word_length == 36:
            return self.input_word
        else:
            raise ValueError(MESSAGES["uuid_length"])
