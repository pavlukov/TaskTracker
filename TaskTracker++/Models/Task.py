class Task:
    def __init__(self, name, content, deadline, category, priority, tags):
        self.name = name
        self.content = content
        self.deadline = deadline
        self.category = category
        self.priority = priority  # the bigger number, the higher priority
        self.status = 0  # -1 - expired, 0 - in process, 1 - done
        self.tags = tags
        self.id = None
