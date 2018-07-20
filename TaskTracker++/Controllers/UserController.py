from DBManagers.UserStorageManager import *
from Models.User import *


class UserController:

    @classmethod
    def register_user(cls, name, password, task_id="", task_list_id=""):
        user = User(name, password, task_id, task_list_id)
        if UserStorageManager.uniq_check(user):
            UserStorageManager.register_user(user)
            print('Пользователь добавлен.')
        else:
            print("Пользователь с таким именем уже существует.")

    @classmethod
    def delete_user(cls, nickname, password):
        user = UserStorageManager.get_user(nickname)
        if user is not None:
            if user.password == password:
                UserStorageManager.delete_user(user)
                print("Пользователь удален.")
            else:
                print("Неверный пароль.")
        else:
            print("Неверный логин.")
