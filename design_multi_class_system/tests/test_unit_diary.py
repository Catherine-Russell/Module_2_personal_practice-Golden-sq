from lib.diary import Diary
import pytest
"""
    diary:
        - list todolist (empty)
        - list contacts before added returns empty dict
        - list reflects on before added returns empty list
        - select_diary_when_busy returns error when none added yet
"""

def test_return_empty_todolist_when_none_added():
    diary = Diary()
    assert diary.show_todo_list() == []

def test_contacts_returns_empty_dict_when_none_added():
    diary = Diary()
    assert diary.show_contacts() == []

def test_show_past_diary_entries_returns_empty_list_when_none_added():
    diary = Diary()
    assert diary.show_past_diary_entries() == []

def test_select_when_busy_raises_error_if_no_diary_entries_added():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.select_entry_when_busy(5, 2)
    err_msg = str(e.value)
    assert err_msg == "No entries to choose from!"