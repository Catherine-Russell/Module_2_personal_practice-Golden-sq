# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        if task == "":
            raise Exception("Task cannot be empty string")
        elif type(task) != str:
            raise Exception("Task must be string type")
        self.task = task
        self.is_complete = False

    def mark_complete(self):
        self.is_complete = True