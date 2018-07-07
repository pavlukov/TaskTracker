from Models.Task import *
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
        task = c.fetchall()
        db.close()
        return task[-1][0]

    @classmethod
    def delete_task(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("DELETE FROM Task WHERE id = '%s'" % id)
        db.commit()
        db.close()

    @classmethod
    def get_task(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM Task WHERE id == '%s'" % id)
        task_args = c.fetchone()
        if task_args is not None:
            task = Task(task_args[0], task_args[1], task_args[2], task_args[3], task_args[4], task_args[6])
            task.id = id
            task.status = task_args[5]
            return task
        else:
            return None

    @classmethod
    def change_task(cls, task):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        print(task.id)
        c.execute("UPDATE Task SET name = '%s', content = '%s', deadline = '%s', category = '%s', "
                  "priority = '%s', status = '%s', tags = '%s' WHERE id = '%s'"
                  % (task.name, task.content, task.deadline, task.category, task.priority,
                     task.status, task.tags, task.id))
        db.commit()
        db.close()
