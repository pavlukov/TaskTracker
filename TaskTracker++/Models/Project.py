class Project:
    def __init__(self, name, owner, task_lists="", tasks="", users=""):
        self.name = name
        self.task_lists = task_lists
        self.tasks = tasks
        self.users = users
        self.owner = owner
        self.id = None
