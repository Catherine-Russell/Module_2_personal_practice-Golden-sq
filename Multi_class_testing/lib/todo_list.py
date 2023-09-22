# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.task_list = []

    def add(self, todo):
        self.task_list.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos

    def incomplete(self):
        incomplete_tasks = [
            str(task.task)
            for task in self.task_list
            if task.is_complete == False
            ]
        return incomplete_tasks

    def complete(self):
        completed_tasks = [task.task for task in self.task_list if task.is_complete == True]
        return completed_tasks

    def give_up(self):
        for task in self.task_list:
            task.mark_complete()
