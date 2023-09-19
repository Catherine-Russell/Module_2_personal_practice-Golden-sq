from lib.personal_diary import *
import pytest

def test_fewer_than_five_words_returns_the_words():
    assert make_snippet("Today was great!") == "Today was great!"

def test_five_words_returns_the_words():
    assert make_snippet("Today was a great day!") == "Today was a great day!"

def test_more_than_five_words_abbreviates():
    assert make_snippet("Dear Diary, today was an absolutely wonderful day alhamdulilah") == "Dear Diary, today was an..."

def test_if_given_empty_return_empty():
    assert make_snippet("") == ""

def test_counting_number_of_words():
    assert count_words("Dear Diary, today was an absolutely wonderful day alhamdulilah") == 9

def test_count_if_string_is_empty():
    assert count_words("") == 0

def test_count_if_string_is_whitespace():
    assert count_words("             ") == 0

def test_count_if_string_is_all_numbers():
    with pytest.raises(Exception) as err:
        count_words("1234246424562437")
    error_message = str(err.value)
    assert error_message == "Please input words, not numbers"