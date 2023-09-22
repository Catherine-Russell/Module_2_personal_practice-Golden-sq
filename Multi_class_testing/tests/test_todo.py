from lib.todo import Todo
import pytest
# create a todo and call from init
# check if todo is complete
# mark a todo as complete

# Edge cases:
    # empty string gives error msg 
    # non-string gives error msg

def test_create_todo_and_check_task_and_if_complete():
    todo1 = Todo("cook dinner")
    assert todo1.task == "cook dinner"
    assert todo1.is_complete == False

def test_create_task_and_mark_compelte():
    todo1 = Todo("cook dinner")
    todo1.mark_complete()
    assert todo1.is_complete == True

def test_empty_string_raises_error():
    with pytest.raises(Exception) as err:
        todo1 = Todo("")
    err_msg = str(err.value)
    assert err_msg == "Task cannot be empty string"

def test_non_string_raises_error():
    with pytest.raises(Exception) as err:
        todo1 = Todo(123)
    err_msg = str(err.value)
    assert err_msg == "Task must be string type"