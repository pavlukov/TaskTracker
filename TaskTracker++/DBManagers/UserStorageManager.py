import sqlite3
from Models.User import User


class UserStorageManager:

    @classmethod
    def register_user(cls, user):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute(
            "INSERT INTO User (nickname, password, task_id) VALUES ('%s', '%s', '%s')" %
            (user.nickname, user.password, user.task_id))
        db.commit()
        db.close()
        return True

    @classmethod
    def uniq_check(cls, user):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM User WHERE nickname = '%s'" % user.nickname)
        user_list = c.fetchall()
        db.close()
        if len(user_list) > 0:
            return False
        else:
            return True

    @classmethod
    def delete_user(cls, user):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("DELETE FROM User WHERE nickname == '%s'" % user.nickname)
        db.commit()
        db.close()

    @classmethod
    def get_user(cls, nickname):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM User WHERE nickname == '%s'" % nickname)
        user_args = c.fetchone()
        if user_args is not None:
            user = User(user_args[0], user_args[1], user_args[2], user_args[3])
            return user
        else:
            return None

    @classmethod
    def change_user(cls, user):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("UPDATE User SET nickname = '%s', password = '%s', task_id = '%s' WHERE user_id = '%s'" %
                  (user.nickname, user.password, user.task_id, user.user_id))
        db.commit()
        db.close()
