from Models.BaseModel import mysql_db
from Models.ChoiceCourse import ChoiceCourse
from Models.Course import Course
from Models.GroupCourse import GroupCourse
from Models.Professor import Professor
from Models.Student import Student
from Models.TimeCourse import TimeCourse
from Seeders.ChoiceCourseTableSeeder import choicecourse_seed
from Seeders.GroupCourseTableSeeder import groupcourse_seed
from Seeders.ProfessorTableSeeder import professor_seed
from Seeders.StudentTableSeeder import student_seed

__author__ = 'hossein moghadam'

from Seeders.TimeCourseTableSeeder import timecourse_seed
from Seeders.CourseTableSeeder import course_seed


def cli(app):
    @app.cli.command('db_seed')
    def db_seed():
        course_seed()
        timecourse_seed()
        professor_seed()
        groupcourse_seed()
        student_seed()
        choicecourse_seed()

    @app.cli.command('migrate')  # TODO: pass error migrate
    def migrate():
        mysql_db.connect()
        mysql_db.create_tables([Student, ChoiceCourse, Course, GroupCourse, Professor, TimeCourse])
