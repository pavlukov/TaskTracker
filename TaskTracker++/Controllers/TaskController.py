from Models.Task import *
from DBManagers.UserStorageManager import *
from DBManagers.TaskStorageManager import *
import time


class TaskController:

    @classmethod
    def task_add(cls, nickname, password, name, content, deadline, category, priority, tags):
        task = Task(name, content, deadline, category, priority, tags)
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                user.task_id += str(TaskStorageManager.add_task(task)) + " "
                UserStorageManager.change_user(user)
                print("Задача добавлена.")
            else:
                print("Неверный пароль.")
        else:
            print("Пользователя с таким именем не существует.")

    @classmethod
    def delete_task(cls, nickname, password, id):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                TaskStorageManager.delete_task_from_user(nickname, id)
                print("Задача удалена.")
            else:
                print("Неверный пароль.")
        else:
            print("Пользователя с таким именем не существует.")