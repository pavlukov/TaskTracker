class Task:
    def __init__(self, name, content, deadline, category, priority, tags):
        self.name = name
        self.content = content
        self.deadline = deadline
        self.category = category
        self.priority = priority
        self.status = 0  # -1 - не выполнена, 0 - выполняется, 1 - выполнена
        self.tags = tags
        self.id = None
