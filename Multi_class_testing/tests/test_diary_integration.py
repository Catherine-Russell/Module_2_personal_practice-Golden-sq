from lib.diary import Diary
from lib.diary_entry import DiaryEntry
import pytest

# 1. add diary entry and call all returns entries list
def test_add_1_entry_and_call_all():
    my_diary = Diary()
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    my_diary.add(entry1)
    assert my_diary.all() == [entry1]

# 2. add 2 diary entries and call all returns entries list
def test_add_2_entries_and_call_all():
    my_diary = Diary()
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    entry2 = DiaryEntry("Tuesday 2nd January", "I have recovered from the hangover and went for a nice long walk along the beach.")
    my_diary.add(entry1)
    my_diary.add(entry2)
    assert my_diary.all() == [entry1, entry2]

# 3. add 2 diary entries and calling countwords total num of words
def test_add_2_entry_and_countwords():
    my_diary = Diary()
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    entry2 = DiaryEntry("Tuesday 2nd January", "I have recovered from the hangover and went for a nice long walk along the beach.")
    my_diary.add(entry1)
    my_diary.add(entry2)
    assert my_diary.count_words() == 30
    
# 4. add 2 diary entries and calling reading_time
def test_add_2_entry_and_reading_time():
    my_diary = Diary()
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    entry2 = DiaryEntry("Tuesday 2nd January", "I have recovered from the hangover and went for a nice long walk along the beach.")
    my_diary.add(entry1)
    my_diary.add(entry2)
    assert my_diary.reading_time(5) == 6

# 5. as above but with diff wpm
def test_add_2_entry_and_reading_time_diff_wpm():
    my_diary = Diary()
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    entry2 = DiaryEntry("Tuesday 2nd January", "I have recovered from the hangover and went for a nice long walk along the beach.")
    my_diary.add(entry1)
    my_diary.add(entry2)
    assert my_diary.reading_time(4) == 8

# 6. best entry for reading time gives closest
def test_best_entry_returns_closest():
    my_diary = Diary()
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    entry2 = DiaryEntry("Tuesday 2nd January", "I have recovered from the hangover and went for a nice long walk along the beach.")
    entry3 = DiaryEntry("Wednesday 3rd January 2023", "Today I ate sushi with Samir")
    my_diary.add(entry1)
    my_diary.add(entry2)
    my_diary.add(entry3)
    assert my_diary.find_best_entry_for_reading_time(5, 2) == "Wednesday 3rd January 2023: Today I ate sushi with Samir"

# 7. best entry for reading time gives closest lower if closest is over the length possible
def test_best_entry_returns_lower_if_closest_is_over():
    my_diary = Diary()
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    entry2 = DiaryEntry("Tuesday 2nd January", "I have recovered from the hangover and went for a nice long walk along the beach.")
    entry3 = DiaryEntry("Wednesday 3rd January 2023", "Today I ate sushi with Samir")
    my_diary.add(entry1)
    my_diary.add(entry2)
    my_diary.add(entry3)
    assert my_diary.find_best_entry_for_reading_time(6, 3) == "Monday 1st January 2023: Today I woke up hungover and unhappy."

    # 8. if no entries close enough raise exception
def test_best_entry_raises_exception_if_nothing_short_enough():
    my_diary = Diary()
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    entry2 = DiaryEntry("Tuesday 2nd January", "I have recovered from the hangover and went for a nice long walk along the beach.")
    entry3 = DiaryEntry("Wednesday 3rd January 2023", "Today I ate sushi with Samir")
    my_diary.add(entry1)
    my_diary.add(entry2)
    my_diary.add(entry3)
    with pytest.raises(Exception) as e:
        my_diary.find_best_entry_for_reading_time(3, 3)
    errmsg = str(e.value)
    assert errmsg == "You don't have any entries which are short enough to read"
