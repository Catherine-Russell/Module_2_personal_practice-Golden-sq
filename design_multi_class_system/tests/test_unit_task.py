"""
task:
    - create a task amd call it
    - create a task and mark it complete
    - empty string returns err
    - non-string returns error
"""
from lib.task import Task
import pytest

def test_create_a_task_and_call_it():
    task1 = Task("Cook dinner")
    assert task1.details == "Cook dinner"
    assert task1.is_complete == False

def test_make_task_and_mark_complete():
    task1 = Task("Cook dinner")
    task1.mark_complete()
    assert task1.is_complete == True

def test_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        task1 = Task("")
    err_msg = str(e.value)
    assert err_msg == "Task cannot be empty string"

def test_non_string_raises_error():
    with pytest.raises(Exception) as e:
        task1 = Task(123)
    err_msg = str(e.value)
    assert err_msg == "Task must be string type"