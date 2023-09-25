class Task():
    def __init__(self, details):
        if details == "":
            raise Exception("Task cannot be empty string")
        elif type(details) != str:
            raise Exception("Task must be string type")
        self.details = details
        self.is_complete = False

    def mark_complete(self):
        self.is_complete = True