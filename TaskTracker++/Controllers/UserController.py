from DBManagers.UserStorageManager import *
from Models.User import *


class UserController:

    @classmethod
    def register_user(cls, name, password, task_id=None):
        user = User(name, password, task_id)
        if UserStorageManager.uniq_check(user):
            if UserStorageManager.register_user(user):
                print('Пользователь добавлен.')
            else:
                print('Ошибка при добавлении пользователя.')
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
            print("Пользователя с таким именем не существует.")