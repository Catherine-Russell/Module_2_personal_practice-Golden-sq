"""
Input / output diagram

add task ==> no return
add task and check the task list ==> [task]
add two task and check the task list ==> [task1,task2]

add two task and remove the second one and call check list ==> [task1]
add two task and remove the fist one and call check list ==> [task2]
remove a task never added ==> return string "choose a task from this list' and then return the list
clear the list - remove more than 1 task ==> []




Edge cases
add empty string ==> raise Exception "task can not be empty string"
wrong type of entry ==> raise Exception "task must be a string type"
"""

from lib.to_do_organiser import *
import pytest

def test_add_a_task():
    tracker = To_do_tracker()
    tracker.add_task("do laundry")
    result = tracker.task_lst
    assert result == ["do laundry"]

def test_add_task_and_call_list():
    tracker = To_do_tracker()
    tracker.add_task("do laundry")
    assert tracker.lst_tasks() == ["do laundry"]

def test_add_two_tasks_and_call_list():
    tracker = To_do_tracker()
    tracker.add_task("do laundry")
    tracker.add_task("cook")
    assert tracker.lst_tasks() == ["do laundry", "cook"]

def test_add_two_task_remove_second_call_check_list():
    tracker = To_do_tracker()
    tracker.add_task("do laundry")
    tracker.add_task("cook")
    tracker.remove_completed_task("do laundry")
    assert tracker.lst_tasks() == ["cook"]

def test_add_two_task_remove_first_call_check_list():
    tracker = To_do_tracker()
    tracker.add_task("do laundry")
    tracker.add_task("cook")
    tracker.remove_completed_task("cook")
    assert tracker.lst_tasks() == ["do laundry"]

def test_remove_more_than_one_task():
    tracker = To_do_tracker()
    tracker.add_task("do laundry")
    tracker.add_task("cook")
    tracker.remove_completed_task("cook")
    tracker.remove_completed_task("do laundry")
    assert tracker.lst_tasks() == []

def test_remove_task_not_in_list():
    tracker = To_do_tracker()
    tracker.add_task("do laundry")
    tracker.add_task("cook")
    assert tracker.remove_completed_task("wash dishes") == "This task is not in your To Do List. Please choose from: ['do laundry', 'cook']"

def test_add_empty_string_raises_error():
    tracker = To_do_tracker()
    with pytest.raises(Exception) as e:
        tracker.add_task("")
    error_message = str(e.value)
    assert error_message == "Task can not be empty string"

def test_add_non_string_type_raises_error():
    tracker = To_do_tracker()
    with pytest.raises(Exception) as e:
        tracker.add_task(1234)
    error_message = str(e.value)
    assert error_message == "Task must be a string"

def test_add_multiple_tasks_sep_with_comma():
    tracker = To_do_tracker()
    tracker.add_multiple_tasks("cooking, sleeping, reading")
    assert tracker.lst_tasks() == ["cooking", "sleeping", "reading"] 

def test_add_multiple_tasks_sep_with_and():
    tracker = To_do_tracker()
    tracker.add_multiple_tasks("cooking, sleeping and reading")
    assert tracker.lst_tasks() == ["cooking", "sleeping", "reading"] 