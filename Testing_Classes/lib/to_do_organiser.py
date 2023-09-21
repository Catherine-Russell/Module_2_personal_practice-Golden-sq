class To_do_tracker():
    def __init__(self):
        self.task_lst = []

    def add_task(self, string):
        #add a new tasl to self.task_list
        #input string type str
        #output None
        if string == "":
            raise Exception("Task can not be empty string")
        elif type(string) != str:
            raise Exception("Task must be a string")
        else:
            self.task_lst.append(string)

    def add_multiple_tasks(self, tasks):
        new_tasks = tasks.split(", ")
        for task in new_tasks:
            if "and" not in task:
                self.add_task(task)
            else:
                
                last_tasks = task.split(" and ")
                for task in last_tasks:
                    self.add_task(task)
    
    def lst_tasks(self):
        #return list of tasks
        # input none
        #output list of stings, type list
        return self.task_lst

    def remove_completed_task(self, task):
        #remove string from task list
        #input task type str
        #output none
        if task in self.task_lst:
            self.task_lst.remove(task)
        else:
            return f"This task is not in your To Do List. Please choose from: {self.task_lst}"