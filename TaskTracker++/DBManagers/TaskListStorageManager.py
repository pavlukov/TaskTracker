import sqlite3
from Models.TaskList import *
from DBManagers.UserStorageManager import *


class TaskListStorageManager:

    @classmethod
    def add_task_list(cls, task_list):
        db = sqlite3.connect("TaskTrackerDB")
        c = db.cursor()
        c.execute("INSERT INTO TaskList (name, deadline, priority, status, tasks) "
                  "VALUES ('%s', '%s', '%s', '%s', '%s')" %
                  (task_list.name, task_list.deadline, task_list.priority, task_list.status, task_list.tasks))
        db.commit()
        c.execute("SELECT id FROM TaskList WHERE name = '%s'" % task_list.name)
        task_list = c.fetchall()[-1]
        db.close()
        return task_list[0]

    @classmethod
    def get_task_list(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM TaskList WHERE id == '%s'" % id)
        task_list_args = c.fetchone()
        if task_list_args is not None:
            task_list = TaskList(task_list_args[0], task_list_args[2], task_list_args[3])
            task_list.id = task_list_args[4]
            task_list.status = task_list_args[1]
            task_list.tasks = task_list_args[5]
            task_list.tasks = task_list_args[5]
            return task_list
        else:
            return None

    @classmethod
    def change_task_list(cls, task_list):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("UPDATE TaskList SET name = '%s', deadline = '%s', priority = '%s',"
                  " status = '%s', tasks = '%s' WHERE id = '%s'" %
                  (task_list.name, task_list.deadline, task_list.priority, task_list.status,
                   task_list.tasks, task_list.id))
        db.commit()
        db.close()
        return

    @classmethod
    def delete_task_list(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("DELETE FROM TaskList WHERE id = '%s'" % id)
        db.commit()
        db.close()

    # returns list of tasks with given sub task id
    @classmethod
    def get_task_lists_with_sub_task(cls, sub_task_id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM TaskList WHERE instr(tasks, '%s ') > 0" % sub_task_id)
        list = c.fetchall()
        db.close()
        return list

