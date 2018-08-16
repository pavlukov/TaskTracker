from enum import Enum
from Controllers.UserController import *
from Controllers.TaskController import *
from Controllers.TaskListController import *
from Controllers.ProjectController import *


class Command(Enum):
    task = 0
    task_list = 1
    project = 2
    user = 3


class Arguments(Enum):
    add = 0
    edit = 1
    remove = 2
    show = 3


def get_command(arg):
    return Command[arg]


def get_arguments(arg):
    return Arguments[arg]


def task_parse(arg):
    #try:
        if arg == Arguments.add:
            TaskController.add_task("Egor", "228", "Уник", "Лаба", "24.08.2018", "Прога", 1, "Универ ИСП Лабы Питон")
        elif arg == Arguments.remove:
            TaskController.delete_task("Egor", "228", "27")
        elif arg == Arguments.edit:
            TaskController.edit_task("Iluha", "228", "21", "Зачет")
        elif arg == Arguments.show:
            TaskController.check_deadline("Egor", "228")
            TaskListController.check_deadline("Egor", "228")
    #except:
     #   print('Ошибка при выполнении операции с задачей.')
    #else:
     #   print('Операция успешно завершена.')


def task_list_parse(arg):
    #try:
        if arg == Arguments.add:
            TaskListController.add_task_list("Egor", "228", "Test", "24.08.2001", 228)
        elif arg == Arguments.remove:
            TaskListController.add_sub_task("Egor", "228", "26", "20")
        elif arg == Arguments.edit:
            TaskListController.delete_sub_task("Egor", "228", "26", "21")
        elif arg == Arguments.show:
            TaskListController.edit_task_list("Egor", "228", "25", tasks="223 5")
    #except:
    #    print('Ошибка при выполнении операции со списком задач.')
    #else:
    #    print('Операция успешно завершена.')


def project_parse(arg):
    #try:
        if arg == Arguments.add:
            ProjectController.add_project("Iluha", "228", "gameway")
        elif arg == Arguments.remove:
            ProjectController.delete_project("Iluha", "228", "4")
        elif arg == Arguments.edit:
            ProjectController.add_user_to_project("Iluha", "228", "6", "11", "23", "24 25")
        elif arg == Arguments.show:
            ProjectController.delete_user_from_project("Iluha", "228", "6", "11")
    #except:
     #   print('Ошибка при выполнении операции с проектом.')
    #else:
     #   print('Операция успешно завершена.')


def user_parse(arg, args):
    try:
        if arg == Arguments.add:
            if len(args) == 3:
                UserController.register_user(args[0], args[1], args[2])
            else:
                UserController.register_user(args[0], args[1])
        elif arg == Arguments.remove:
            UserController.delete_user(args[0], args[1])
        elif arg == Arguments.edit:
            print("user edit")
    except:
        print('Ошибка при выполнении операции с пользователем.')


def parse(args):
    if len(args) >= 2:
        try:
            command = get_command(args[0])
        except KeyError as e:
            print('Команда {} не найдена.'.format(e))
        else:
            try:
                argument = get_arguments(args[1])
            except KeyError as e:
                print('Неверный аргумент: {}.'.format(e))
            else:
                if command == Command.task:
                    task_parse(argument)
                elif command == Command.task_list:
                    task_list_parse(argument)
                elif command == Command.project:
                    project_parse(argument)
                elif command == Command.user:
                    user_parse(argument, args[2::])

    else:
        print('Неверное количество аргументов.')

