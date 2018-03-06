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
        # course_seed()
        # timecourse_seed()
        # professor_seed()
        # groupcourse_seed()
        student_seed()
        choicecourse_seed()