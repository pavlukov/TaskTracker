from Models.Task import *
from DBManagers.UserStorageManager import *
from DBManagers.TaskStorageManager import *
from DBManagers.TaskListStorageManager import *
from DBManagers.ProjectStorageManager import *


class TaskController:
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
            print("Неверный логин.")

    @classmethod
    def delete_task(cls, nickname, password, id):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                if TaskStorageManager.get_task(id) is None:
                    print("Задача не найдена.")
                    return
                user.task_id = user.task_id.replace('%s ' % id, '')
                UserStorageManager.change_user(user)
                if len(UserStorageManager.get_users_with_task(id)) == 0 and \
                                len(TaskListStorageManager.get_task_lists_with_sub_task(id)) == 0 and \
                                len(ProjectStorageManager.get_project_with_task(id)) == 0:
                    TaskStorageManager.delete_task(id)
                print("Задача удалена.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def edit_task(cls, nickname, password, id, name=None, content=None, deadline=None, category=None,
                  priority=None, status=None, tags=None):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                task = TaskStorageManager.get_task(id)
                if task is None or UserStorageManager.get_users_with_task(id) is None:
                    print("Задача не найдена.")
                    return
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
            print("Неверный логин.")

    @classmethod
    def set_task_status(cls, nickname, password, task_id, status):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                task = TaskStorageManager.get_task(task_id)
                if task is None or UserStorageManager.get_users_with_task(task_id) is None:
                    print("Задача не найдена.")
                    return
                task.status = status
                TaskStorageManager.change_task(task)
                if status == -1:
                    print("Задача не выполнена.")
                elif status == 1:
                    print("Задача выполнена.")
                else:
                    print("Задача выполняется.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def check_deadline(cls, nickname, password):
        user = UserStorageManager.get_user(nickname)
        if user.password == password:
            current_date = datetime.datetime.now()
            tasks = user.task_id.split(" ")[:-1]
            for task_id in tasks:
                task = TaskStorageManager.get_task(task_id)
                if task.status == 0:
                    time_remaining = task.deadline_from_str_to_datetime(task.deadline) - current_date
                    if time_remaining.days <= 5:
                        print("\n*ОПОВЕЩАНИЕ*\n%s(%s) осталось %s дней, %s часов." %
                              (task.name, task.id, time_remaining.days, round(time_remaining.seconds/3600)))
                    if time_remaining.days < 0:
                        task.status = -1
                        TaskStorageManager.change_task(task)
                        print("\n*ОПОВЕЩАНИЕ*\nЗадача %s(%s) не выполнена.\n" % (task.name, task.id))
            project_tasks = user.project_task_id.split(" ")[:-1]
            for project_task_id in project_tasks:
                project_task = TaskStorageManager.get_task(project_task_id)
                if project_task.status == 0:
                    time_remaining = project_task.deadline_from_str_to_datetime(project_task.deadline) - current_date
                    if time_remaining.days <= 5:
                        print("\n*ОПОВЕЩАНИЕ*\n%s(%s) осталось %s дней, %s часов." %
                              (project_task.name, project_task.id,
                               time_remaining.days, round(time_remaining.seconds/3600)))
                    if time_remaining.days < 0:
                        project_task.status = -1
                        TaskStorageManager.change_task(project_task)
                        print("\n*ОПОВЕЩАНИЕ*\nЗадача %s(%s) не выполнена.\n" % (project_task.name, project_task.id))
