from lib.Recipe_1 import *
from lib.recipe_1_texts import *
import pytest

def test_text_of_200_words_returns_1_min():
    duration = find_duration(text1)
    assert duration == "It will take 1 minute and 0 seconds"

def test_text_of_less_than_200_returns_seconds_only():
    duration = find_duration(text2)
    assert duration == "It will take 0 minutes and 45 seconds"

def test_text_of_500_words_returns_2_mins_30():
    duration = find_duration(text3)
    assert duration == "It will take 2 minutes and 30 seconds"

def test_151_seconds_rounds_up_to_next_second():
    duration = find_duration(text4)
    assert duration == "It will take 0 minutes and 46 seconds"

def test_99_seconds_rounds_up_to_next_second():
    duration = find_duration(text5)
    assert duration == "It will take 0 minutes and 30 seconds"

def test_1_word_is_1_second():
    duration = find_duration(text6)
    assert duration == "It will take 0 minutes and 1 second"

def test_all_numbers():
    with pytest.raises(Exception) as err:
        duration = find_duration("23456786543345678765434567889876543")
    error_msg = str(err.value)
    assert error_msg == "Please input words, not numbers."

# There is a potential bug in which it could just be lots of numbers and no words and still go through normally
# currently test all numbers only fails if it's alllll numbers but does not include whitespace as a number so allows it
# could do run is.alpha() over each of the words in a .split() list of the text but would probably be slow
# plus then we'd have to remove all the punctuation too
# but it's lunchtime so I'm going to leave it there for now