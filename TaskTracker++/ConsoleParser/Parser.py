from enum import Enum


class Command(Enum):
    task = 0
    task_list = 1
    project = 2
    user = 3


class Arguments(Enum):
    add = 0
    remove = 1
    edit = 2
    show = 3


def get_command(arg):
    return Command[arg]


def get_arguments(arg):
    return Arguments[arg]


def task_parse(arg):
    try:
        if arg == Arguments.add:
            print("task add")
        elif arg == Arguments.remove:
            print("task remove")
        elif arg == Arguments.edit:
            print("task edit")
        elif arg == Arguments.show:
            print("task show")
    except:
        print('Ошибка при выполнении операции.')
    else:
        print('Операция успешно завершена.')


def task_list_parse(arg):
    try:
        if arg == Arguments.add:
            print("task list add")
        elif arg == Arguments.remove:
            print("task list remove")
        elif arg == Arguments.edit:
            print("task list edit")
        elif arg == Arguments.show:
            print("task list show")
    except:
        print('Ошибка при выполнении операции.')
    else:
        print('Операция успешно завершена.')


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
        print('Ошибка при выполнении операции.')
    else:
        print('Операция успешно завершена.')


def user_parse(arg):
    try:
        if arg == Arguments.add:
            print("user add")
        elif arg == Arguments.remove:
            print("user remove")
        elif arg == Arguments.edit:
            print("user edit")
        elif arg == Arguments.show:
            print("user show")
    except:
        print('Ошибка при выполнении операции.')
    else:
        print('Операция успешно завершена.')


def parse(args):
    if len(args) == 2:
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
                    user_parse(argument)

    else:
        print('Неверное количество аргументов.')

