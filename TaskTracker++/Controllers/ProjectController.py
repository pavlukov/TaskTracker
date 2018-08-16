from DBManagers.UserStorageManager import *
from DBManagers.ProjectStorageManager import *
from DBManagers.TaskListStorageManager import *
from DBManagers.TaskStorageManager import *

class ProjectController:

    @classmethod
    def add_project(cls, nickname, password, name, task_lists="", users=""):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                project = Project(name, user.user_id, task_lists, users)
                user.project_id += str(ProjectStorageManager.add_project(project)) + " "
                UserStorageManager.change_user(user)
                print("Проект добавлен.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def add_user_to_project(cls, nickname, password, project_id, user_id, project_task_id="", project_task_list_id=""):
        owner = UserStorageManager.get_user(nickname)
        if owner is not None:
            if owner.password == password:
                project = ProjectStorageManager.get_project(project_id)
                if project is None:
                    print("Проект не найден.")
                    return
                if owner.user_id == project.owner:
                    if project.users.count("%s " % user_id) > 0 or user_id == str(project.owner):
                        print("Пользователь уже добавлен в проект.")
                        return
                    user = UserStorageManager.get_user_by_id(user_id)
                    if user is None:
                        print("Пользователь не найден.")
                        return
                    project.users += str(user_id) + " "
                    ProjectStorageManager.change_project(project)
                    user.project_task_id += project_task_id + " "
                    user.project_task_list_id += project_task_list_id + " "
                    UserStorageManager.change_user(user)
                    print("Пользователь добавлен в проект.")
                else:
                    print("Вы не являетесь владельцем проекта.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def add_task_to_project(cls, nickname, password, project_id, task_id):
        owner = UserStorageManager.get_user(nickname)
        if owner is not None:
            if owner.password == password:
                project = ProjectStorageManager.get_project(project_id)
                if project is None:
                    print("Проект не найден.")
                    return
                if owner.user_id == project.owner:
                    if project.tasks.count("%s " % task_id) > 0:
                        print("Задача уже добавлена в проект.")
                        return
                    if TaskStorageManager.get_task(task_id) is None:
                        print("Задача не найдена.")
                        return
                    project.tasks += str(task_id) + " "
                    ProjectStorageManager.change_project(project)
                    print("Задача добавлена в проект.")
                else:
                    print("Вы не являетесь владельцем проекта.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def add_task_list_to_project(cls, nickname, password, project_id, task_list_id):
        owner = UserStorageManager.get_user(nickname)
        if owner is not None:
            if owner.password == password:
                project = ProjectStorageManager.get_project(project_id)
                if project is None:
                    print("Проект не найден.")
                    return
                if owner.user_id == project.owner:
                    if project.task_lists.count("%s " % task_list_id) > 0:
                        print("Список задач уже добавлен в проект.")
                        return
                    if TaskListStorageManager.get_task_list(task_list_id) is None:
                        print("Список задач не найден.")
                        return
                    project.task_lists += str(task_list_id) + " "
                    ProjectStorageManager.change_project(project)
                    print("Список задач добавлен в проект.")
                else:
                    print("Вы не являетесь владельцем проекта.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def delete_project(cls, nickname, password, id):
        owner = UserStorageManager.get_user(nickname)
        if owner is not None:
            if owner.password == password:
                project = ProjectStorageManager.get_project(id)
                if project is None:
                    print("Проект не найден.")
                    return
                if owner.user_id == project.owner:
                    owner.project_id = owner.project_id.replace('%s ' % id, '')
                    UserStorageManager.change_user(owner)
                    ProjectStorageManager.delete_project(id)
                    print("Проект удален.")
                else:
                    print("Вы не являетесь владельцем проекта.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def delete_user_from_project(cls, nickname, password, project_id, user_id):
        owner = UserStorageManager.get_user(nickname)
        if owner is not None:
            if owner.password == password:
                project = ProjectStorageManager.get_project(project_id)
                if project is None:
                    print("Проект не найден.")
                    return
                if owner.user_id == project.owner:
                    if project.users.count("%s " % user_id) == 0:
                        print("Пользователь не найден.")
                        return
                    project.users = project.users.replace('%s ' % user_id, '')
                    ProjectStorageManager.change_project(project)
                    tasks = project.tasks.split(" ")[:-1]
                    task_lists = project.task_lists.split(" ")[:-1]
                    user = UserStorageManager.get_user_by_id(user_id)
                    for task in tasks:
                        user.project_task_id = user.project_task_id.replace("%s " % task, "")
                    for task_list in task_lists:
                        user.project_task_list_id = user.project_task_list_id.replace("%s " % task_list, '')
                    UserStorageManager.change_user(user)
                    print("Пользователь удален из проекта.")
                else:
                    print("Вы не являетесь владельцем проекта.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def delete_task_from_project(cls, nickname, password, project_id, task_id):
        owner = UserStorageManager.get_user(nickname)
        if owner is not None:
            if owner.password == password:
                project = ProjectStorageManager.get_project(project_id)
                if project is None:
                    print("Проект не найден.")
                    return
                if owner.user_id == project.owner:
                    if project.tasks.count("%s " % task_id) == 0:
                        print("Задача не найдена.")
                        return
                    project.tasks = project.tasks.replace('%s ' % task_id, '')
                    ProjectStorageManager.change_project(project)
                    print("Задача удалена из проекта.")
                else:
                    print("Вы не являетесь владельцем проекта.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")

    @classmethod
    def delete_task_list_from_project(cls, nickname, password, project_id, task_list_id):
        owner = UserStorageManager.get_user(nickname)
        if owner is not None:
            if owner.password == password:
                project = ProjectStorageManager.get_project(project_id)
                if project is None:
                    print("Проект не найден.")
                    return
                if owner.user_id == project.owner:
                    if project.task_lists.count("%s " % task_list_id) == 0:
                        print("Список задач не найден.")
                        return
                    project.task_lists = project.task_lists.replace('%s ' % task_list_id, '')
                    ProjectStorageManager.change_project(project)
                    print("Список задач удален из проекта.")
                else:
                    print("Вы не являетесь владельцем проекта.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")
