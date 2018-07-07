class TaskList:
    def __init__(self, name, deadline, priority, task=""):
        self.name = name
        self.status = 0  # -1 - expired, 0 - in process, 1 - done
        self.deadline = deadline
        self.priority = priority  # the bigger number, the higher priority
        self.id = None
        self.tasks = str(task)
