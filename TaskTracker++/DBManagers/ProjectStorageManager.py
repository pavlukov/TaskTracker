import sqlite3
from Models.Project import *


class ProjectStorageManager:

    @classmethod
    def add_project(cls, project):
        db = sqlite3.connect("TaskTrackerDB")
        c = db.cursor()
        c.execute("INSERT INTO Project (name, task_lists, users, owner_id, tasks) "
                  "VALUES ('%s', '%s','%s', '%s', '%s')" %
                  (project.name, project.task_lists, project.users, project.owner, project.tasks))
        db.commit()
        c.execute("SELECT id FROM project WHERE name = '%s'" % project.name)
        project_id = c.fetchall()
        db.close()
        return project_id[-1][0]

    @classmethod
    def get_project(cls, id):
        db = sqlite3.connect("TaskTrackerDB")
        c = db.cursor()
        c.execute("SELECT * FROM Project WHERE id = '%s'" % id)
        project_args = c.fetchone()
        db.close()
        if project_args is not None:
            project = Project(project_args[0], project_args[3], project_args[1], project_args[5], project_args[2])
            project.id = project_args[4]
            return project
        else:
            return None

    @classmethod
    def get_project_with_task(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM Project WHERE instr(tasks, '%s ') > 0" % id)
        projects = c.fetchall()
        db.close()
        return projects

    @classmethod
    def get_project_with_task_list(cls, id):
        db = sqlite3.connect('TaskTrackerDB')
        c = db.cursor()
        c.execute("SELECT * FROM Project WHERE instr(task_lists, '%s ') > 0" % id)
        projects = c.fetchall()
        db.close()
        return projects

    @classmethod
    def change_project(cls, project):
        db = sqlite3.connect("TaskTrackerDB")
        c = db.cursor()
        c.execute("UPDATE Project SET name = '%s', tasks = '%s', task_lists = '%s', owner_id = '%s', "
                  "users = '%s' WHERE id = '%s'"
                  % (project.name, project.tasks, project.task_lists, project.owner, project.users, project.id))
        db.commit()
        db.close()

    @classmethod
    def delete_project(cls, id):
        db = sqlite3.connect("TaskTrackerDB")
        c = db.cursor()
        c.execute("DELETE FROM Project WHERE id = '%s'" % id)
        db.commit()
        db.close()
