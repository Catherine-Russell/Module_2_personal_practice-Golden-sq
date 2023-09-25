from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.task import Task
"""
3. Integration tests:
    - add diary entries and reflect on diary ==> [entry1, entry2, entry3]
    - add diary entries and select one for when busy ==> returns entry closest in time to read but without going over
    - add diary entries and select one for when busy ==> returns entry closest in time to read but without going over WHEN closest is just over
    - add contact and see contacts ==> {name1:number1, name2:number2}
    - add tasks and see in todo list ==> [task1, task2, task3]
    - add tasks, mark 1 complete and see todo list without that one ==> [task1, task3]
    - 
"""

def test_add_diary_entries_and_show_entries_in_list():
    diary = Diary()
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover.")
    entry2 = DiaryEntry("Tuesday 2nd January", "Today was the first day back at work for the new year.")
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    assert diary.show_past_diary_entries() == [entry1, entry2]

def test_select_entry_when_busy_exact_word_count():
    diary = Diary()
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover.")
    entry3 = DiaryEntry("Tuesday 2nd January", "Today was the first day back at work for the new year.")
    entry2 = DiaryEntry("Wednesday 3rd January", "Today I began to truly embrace the new year and have started making significant steps towards the successful achievement of my new year resolution.")
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    diary.add_diary_entry(entry3)
    assert diary.select_entry_when_busy(3, 10) == entry2

def test_select_entry_when_busy_chooses_closest_without_going_over():
    diary = Diary()
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover.")
    entry2 = DiaryEntry("Tuesday 2nd January", "Today was the first day back at work for the new year.")
    entry3 = DiaryEntry("Wednesday 3rd January", "Today I began to truly embrace the new year and have started making significant steps towards the successful achievement of my new year resolution.")
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    diary.add_diary_entry(entry3)
    assert diary.select_entry_when_busy(4, 5) == entry2

def test_find_and_return_phone_numbers_in_entries():
    diary = Diary()
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover. 07783123453")
    diary.add_diary_entry(entry1)
    assert diary.show_contacts() == ["07783123453"]

def test_find_and_return_phone_numbers_in_two_entries():
    diary = Diary()
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover. 07783123453")
    entry2 = DiaryEntry("Tuesday 2nd January", "Today 07722123456 was the first day back at work for the new year.")
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    assert diary.show_contacts() == ["07783123453","07722123456"]

def test_find_and_return_phone_number_in_two_entries():
    diary = Diary()
    entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover.")
    entry2 = DiaryEntry("Tuesday 2nd January", "Today 07722123456 was the first day back at work for the new year.")
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    assert diary.show_contacts() == ["07722123456"]

def test_add_task_and_show_todo_list():
    diary = Diary()
    task1 = Task("cook dinner")
    diary.add_task(task1)
    assert diary.show_todo_list() == ["cook dinner"]

def test_add_two_tasks_and_show_todo_list():
    diary = Diary()
    task1 = Task("cook dinner")
    task2 = Task("do laundry")
    diary.add_task(task1)
    diary.add_task(task2)
    assert diary.show_todo_list() == ["cook dinner", "do laundry"]

def test_add_two_tasks_and_mark_one_complete():
    diary = Diary()
    task1 = Task("cook dinner")
    task2 = Task("do laundry")
    diary.add_task(task1)
    diary.add_task(task2)
    task2.mark_complete()
    assert diary.show_todo_list() == ["cook dinner"]