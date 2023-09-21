"""
Input / output diagram

add task ==> no return
add task and check the task list ==> [task]
add two task and check the task list ==> [task1,task2]

add two task and remove the second one and call check list ==> [task1]
add two task and remove the fist one and call check list ==> [task2]
remove a task never added ==> return string "choose a task from thisn list' and then return the list

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


