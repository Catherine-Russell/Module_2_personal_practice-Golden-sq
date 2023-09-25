"""
    diary_entry:
        - make diary entry and call info
        - make entry and check word count
        - make diary entry and return how long it will take to read (input wpm)
"""
from lib.diary_entry import DiaryEntry
def test_make_diary_entry_and_call_attributes():
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover.")
    assert entry1.date == "Monday 1st January"
    assert entry1.contents == "Today I woke up tired and hungover."

def test_entry_and_check_word_count():
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover.")
    assert entry1.word_count() == 10

def test_make_entry_and_return_how_long_it_takes_to_read():
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover.")
    result = entry1.reading_duration(5)
    assert result == 2

def test_make_entry_and_return_how_long_it_takes_to_read_rounds_up():
    entry1 = DiaryEntry("Monday 1st January", "This morning I woke up tired and hungover.")
    assert entry1.reading_duration(5) == 3
