from lib.todo_list import *
import pytest

def test_string_commencing_in_TODO_returns_true():
    assert check_if_todo("TODO: Clean the bathroom.") == True

def test_string_commencing_in_to_do_returns_true():
    assert check_if_todo("To do: Clean the bathroom.") == True

def test_lowercase_todo_returns_true():
    assert check_if_todo("todo: Clean the bathroom.") == True

def test_title_case_to_do_returns_true():
    assert check_if_todo("To Do: Clean the bathroom.") == True

def test_multiple_sentences_todo_in_second_returns_true():
    assert check_if_todo("Today is Wednesday. TODO list = go to the shops") == True

def test_string_with_no_todo_returns_false():
    assert check_if_todo("Today is Wednesday.") == False

def test_multiple_sentence_string_with_no_todo_returns_false():
    assert check_if_todo("Today is Wednesday. Tomorrow will be Thursday. Then Friday comes after.") == False

def test_string_with_todo_as_part_of_word_returns_false():
    assert check_if_todo("I have a pet pentodon.") == False

def test_string_with_to_do_as_part_of_word_returns_false():
    assert check_if_todo("Let's go to dot's house today!") == False

def test_empty_string_gives_error():
    with pytest.raises(Exception) as err:
        check_if_todo("")
    error_msg = str(err.value)
    assert error_msg == "Text cannot be empty"

def test_string_not_at_beginning_with_todo_returns_true():
    assert check_if_todo("Today is Wednesday so my todo is to go to band practice") == True

def test_string_not_at_beginning_with_to_do_returns_true():
    assert check_if_todo("Laundry is my to do") == True