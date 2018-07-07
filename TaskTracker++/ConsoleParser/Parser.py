from enum import Enum
from Controllers.UserController import *
from Controllers.TaskController import *
from Controllers.TaskListController import *


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
    try:
        if arg == Arguments.add:
            TaskController.add_task("Iluha", "228", "АВС", "Сдать зачет", "02.07.2018", "Прога", 1, "Универ ИСП Лабы Питон")
        elif arg == Arguments.remove:
            TaskController.delete_task("Iluha", "228", "22")
        elif arg == Arguments.edit:
            TaskController.edit_task("Iluha", "228", "21", "Зачет")
        elif arg == Arguments.show:
            print("task show")
    except:
        print('Ошибка при выполнении операции с задачей.')
    else:
        print('Операция успешно завершена.')


def task_list_parse(arg):
    #try:
        if arg == Arguments.add:
            TaskListController.add_task_list("Egor", "228", "Test", "01.01.2001", 228)
        elif arg == Arguments.remove:
            TaskListController.add_sub_task("Egor", "228", "26", "20")
        elif arg == Arguments.edit:
            TaskListController.delete_sub_task("Egor", "228", "26", "21")
        elif arg == Arguments.show:
            print("task list show")
    #except:
    #    print('Ошибка при выполнении операции со списком задач.')
    #else:
    #    print('Операция успешно завершена.')


def project_parse(arg):
    try:
        if arg == Arguments.add:
            print("project add")
        elif arg == Arguments.remove:
            print("project remove")
        elif arg == Arguments.edit:
            print("project edit")
        elif arg == Arguments.show:
            print("project show")
    except:
        print('Ошибка при выполнении операции с проектом.')
    else:
        print('Операция успешно завершена.')


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

