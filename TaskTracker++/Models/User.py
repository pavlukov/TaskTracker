class User:
    def __init__(self, nickname, password, user_id=None, task_id="", task_list_id=""):
        self.nickname = nickname
        self.password = password
        self.task_id = task_id
        self.task_list_id = task_list_id
        self.user_id = user_id
