import datetime


class Task:
    def __init__(self, name, content, deadline="", category="", priority="", tags=""):
        self.name = name
        self.content = content
        if deadline != "":
            self.deadline = Task.deadline_from_str_to_datetime(deadline).strftime("%d.%m.%Y")
        else:
            self.deadline = None
        self.category = category
        self.priority = priority  # the bigger number, the higher priority
        self.status = 0  # -1 - expired, 0 - in process, 1 - done
        self.tags = tags
        self.id = None

    @classmethod
    def deadline_from_str_to_datetime(cls, deadline_str):
        deadline_args = deadline_str.split(".")
        deadline = datetime.datetime(int(deadline_args[2]), int(deadline_args[1]), int(deadline_args[0]))
        return deadline
