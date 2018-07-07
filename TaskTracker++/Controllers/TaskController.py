from Models.Task import *
from DBManagers.UserStorageManager import *
from DBManagers.TaskStorageManager import *
import time


class TaskController:
    # TODO: пофиксить УДАЛЕНИЕ ТАСКИ (ЧТОБЫ ПРОВЕРКА ЗАПСУКАЛАСЬ ДО УДАЛЕНИЯ)
    @classmethod
    def add_task(cls, nickname, password, name, content, deadline, category, priority, tags):
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
                if len(UserStorageManager.get_users_with_task(id)) == 0:
                    print("Задача не найдена.")
                    return
                user.task_id = user.task_id.replace('%s ' % id, '')
                UserStorageManager.change_user(user)
                if len(UserStorageManager.get_users_with_task(id)) == 0:
                    TaskStorageManager.delete_task(id)
                print("Задача удалена.")
            else:
                print("Неверный пароль.")
        else:
            print("Пользователя с таким именем не существует.")

    @classmethod
    def edit_task(cls, nickname, password, id, name=None, content=None, deadline=None, category=None,
                  priority=None, status=None, tags=None):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                task = TaskStorageManager.get_task(id)
                print(task.name, task.content, task.deadline, task.category, task.priority, task.status, task.tags, task.id)
                if name is not None:
                    task.name = name
                if content is not None:
                    task.content = content
                if deadline is not None:
                    task.deadline = deadline
                if category is not None:
                    task.category = category
                if priority is not None:
                    task.priority = priority
                if status is not None:
                    task.status = status
                if tags is not None:
                    task.tags = tags
                TaskStorageManager.change_task(task)
                print("Задача изменена.")
            else:
                print("Неверный пароль.")
        else:
            print("Пользователя с таким именем не существует.")


