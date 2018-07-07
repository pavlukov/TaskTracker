from DBManagers.TaskListStorageManager import *
from DBManagers.UserStorageManager import *
from DBManagers.TaskStorageManager import *
from Models.TaskList import *


class TaskListController:

    @classmethod
    def add_task_list(cls, nickname, password, name, deadline, priority, task=None):
        if task is not None:
            task_list = TaskList(name, deadline, priority, str(task) + " ")
        else:
            task_list = TaskList(name, deadline, priority)
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                user.task_list_id += str(TaskListStorageManager.add_task_list(task_list)) + " "
                UserStorageManager.change_user(user)
                print("Список задач добавлен.")
            else:
                print("Неверный пароль.")
        else:
            print("Пользователя с таким именем не существует.")

    @classmethod
    def add_sub_task(cls, nickname, password, task_list_id, task_id):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                task_list = TaskListStorageManager.get_task_list(task_list_id)
                if task_list is None:
                    print("Список задач не найден.")
                    return
                task = TaskStorageManager.get_task(task_id)
                if task is not None:
                    task_list.tasks += str(task_id) + " "
                    TaskListStorageManager.change_task_list(task_list)
                    print("Подзадача добавлена.")
                else:
                    print("Задача не найдена.")
            else:
                print("Неверный пароль.")
        else:
            print("Пользователя с таким именем не существует.")

    @classmethod
    def delete_task_list(cls, nickname, password, id):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                UserStorageManager.get_user(nickname)
                user.task_list_id = user.task_list_id.replace('%s ' % id, '')
                UserStorageManager.change_user(user)
                if len(UserStorageManager.get_users_with_task_list(id)) == 0:
                    TaskListStorageManager.delete_task_list(id)
                print("Список задач удален.")
            else:
                print("Неверный пароль.")
        else:
            print("Пользователя с таким именем не существует.")

    @classmethod
    def delete_sub_task(cls, nickname, password, task_list_id, sub_task_id):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                task_list = TaskListStorageManager.get_task_list(task_list_id)
                task_list.tasks = task_list.tasks.replace('%s ' % sub_task_id, '')
                TaskListStorageManager.change_task_list(task_list)
                if len(TaskListStorageManager.get_task_lists_with_sub_task(sub_task_id)) == 0 \
                        and len(UserStorageManager.get_users_with_task(sub_task_id)) == 0:
                    TaskStorageManager.delete_task(sub_task_id)
                print("Подзадача удалена.")
            else:
                print("Неверный пароль.")
        else:
            print("Пользователя с таким именем не существует.")
