from lib.todo_list import TodoList
# test Todolist returns empty complete and incomplete list when nothing added


def test_empty_complete_lists_when_nothing_added():
    tasktracker = TodoList()
    assert tasktracker.incomplete() == []

def test_empty_incomplete_lists_when_nothing_added():
    tasktracker = TodoList()
    assert tasktracker.complete() == []

