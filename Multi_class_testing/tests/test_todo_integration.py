from lib.todo import Todo
from lib.todo_list import TodoList
# test Todolist add a todo
# test todo list marks 2 todos and returns them in incomplete list
# test todo list adds 2 todos and marks 1 as complete ==> return both complete and incomplete lists
# test todo list adds todo, marks as complete then add 1 more ==> return complete and incomplete lists
# 

# test todolist markcomplete

def test_add_a_todo():
    mytracker = TodoList()
    task1 = Todo("cook dinner")
    mytracker.add(task1)
    assert mytracker.incomplete() == ["cook dinner"]
    assert mytracker.complete() == []

def test_add_two_todos():
    mytracker = TodoList()
    task1 = Todo("cook dinner")
    task2 = Todo("hang laundry")
    mytracker.add(task1)
    mytracker.add(task2)
    assert mytracker.incomplete() == ["cook dinner", "hang laundry"]
    assert mytracker.complete() == []

def test_add_two_todos_and_mark_one_complete():
    mytracker = TodoList()
    task1 = Todo("cook dinner")
    task2 = Todo("hang laundry")
    mytracker.add(task1)
    mytracker.add(task2)
    task2.mark_complete()
    assert mytracker.incomplete() == ["cook dinner"]
    assert mytracker.complete() == ["hang laundry"]

def test_give_up_turns_all_tasks_to_complete():
    mytracker = TodoList()
    task1 = Todo("cook dinner")
    task2 = Todo("hang laundry")
    task3 = Todo("Go to shops")
    mytracker.add(task1)
    mytracker.add(task2)
    mytracker.add(task3)
    assert mytracker.incomplete() == ["cook dinner", "hang laundry", "Go to shops"]
    assert mytracker.complete() == []
    mytracker.give_up()
    assert mytracker.complete() == ["cook dinner", "hang laundry", "Go to shops"]
    assert mytracker.incomplete() == []
