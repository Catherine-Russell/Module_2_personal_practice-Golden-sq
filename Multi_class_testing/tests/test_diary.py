from lib.diary import Diary
import pytest

# 1. calling all when nothing added gives empty list
def test_calling_all_when_nothing_added_returns_empty_list():
    mydiary = Diary()
    assert mydiary.all() == []

# 2. calling countwords when nothing added gives 0
def test_calling_countwords_when_nothing_added_returns_0():
    mydiary = Diary()
    assert mydiary.count_words() == 0

# 3. calling reading_time when nothing added gives 0
def test_calling_reading_time_when_nothing_added_returns_0():
    mydiary = Diary()
    assert mydiary.reading_time(5) == 0

# 4. calling best entry for reading time when none available raises exception
def test_calling_best_entry_when_nothing_added_raises_exception():
    mydiary = Diary()
    with pytest.raises(Exception) as e:
        mydiary.find_best_entry_for_reading_time(5, 7)
    error_msg = str(e.value)
    assert error_msg == "You currently have no entries"