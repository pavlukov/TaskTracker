from Models.Task import *
from Models.User import *
from DBManagers.UserStorageManager import *
import sqlite3


class TaskStorageManager:

    @classmethod
    def add_task(cls, task):
        db = sqlite3.connect("TaskTrackerDB")
        c = db.cursor()
        c.execute("INSERT INTO Task (name, content, deadline, category, priority, status, tags) "
                  "VALUES ('%s', '%s','%s', '%s', '%s', '%s', '%s')" %
                  (task.name, task.content, task.deadline, task.category, task.priority, task.status, task.tags))
        db.commit()
        c.execute("SELECT id FROM Task WHERE content = '%s'" % task.content)
        task = c.fetchone()
        db.close()
        return task[0]

    @classmethod
    def delete_task_from_user(cls, nickname, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM User WHERE nickname = '%s'" % nickname)
        args = c.fetchone()
        user = User(args[0], args[1], args[2], args[3])
        user.task_id = user.task_id.replace('%s ' % id, '')
        UserStorageManager.change_user(user)
        c.execute("SELECT * FROM User WHERE instr(task_id, '%s ') > 0" % id)
        list = c.fetchall()
        if len(list) == 0:
            TaskStorageManager.delete_task(id)
        db.commit()
        db.close()

    @classmethod
    def delete_task(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("DELETE FROM Task WHERE id = '%s'" % id)
        db.commit()
        db.close()
