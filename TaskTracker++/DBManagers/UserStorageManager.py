import sqlite3
from Models.User import User


class UserStorageManager:

    @classmethod
    def register_user(cls, user):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute(
            "INSERT INTO User (nickname, password, task_id, task_list_id, project_id, project_task_id, "
            "project_task_list_id) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %
            (user.nickname, user.password, user.task_id, user.task_list_id, user.project_id,
             user.project_task_id, user.project_task_list_id))
        db.commit()
        db.close()

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
            user = User(user_args[0], user_args[1], user_args[2], user_args[3],
                        user_args[4], user_args[5], user_args[6], user_args[7])
            return user
        else:
            return None

    @classmethod
    def get_user_by_id(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM User WHERE user_id == '%s'" % id)
        user_args = c.fetchone()
        if user_args is not None:
            user = User(user_args[0], user_args[1], user_args[2], user_args[3],
                        user_args[4], user_args[5], user_args[6], user_args[7])
            return user
        else:
            return None

    @classmethod
    def change_user(cls, user):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("UPDATE User SET nickname = '%s', password = '%s', task_id = '%s', user_id = '%s', task_list_id = "
                  "'%s', project_id = '%s', project_task_id = '%s', project_task_list_id = '%s' WHERE user_id = '%s'" %
                  (user.nickname, user.password, user.task_id, user.user_id, user.task_list_id, user.project_id,
                   user.project_task_id, user.project_task_list_id, user.user_id))
        db.commit()
        db.close()

    # returns list of users with given task id
    @classmethod
    def get_users_with_task(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM User WHERE instr(task_id, '%s ') > 0" % id)
        users = c.fetchall()
        db.close()
        return users

    # returns list of users with given task list id
    @classmethod
    def get_users_with_task_list(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM User WHERE instr(task_list_id, '%s ') > 0" % id)
        users = c.fetchall()
        db.close()
        return users

    @classmethod
    def get_users_with_project_id(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM User WHERE instr(project_id, '%s ') > 0" % id)
        users = c.fetchall()
        db.close()
        return users
