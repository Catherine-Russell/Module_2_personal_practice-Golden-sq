class To_do_tracker():
    def __init__(self):
        self.task_lst = []

    def add_task(self, string):
        #add a new tasl to self.task_list
        #input string type str
        #output None
        self.task_lst .append(string)
    
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