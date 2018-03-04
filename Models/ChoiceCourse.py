__author__ = 'hossein moghadam'
from Models.BaseModel import BaseModel, EnumField
from peewee import IntegerField, TextField, CharField, PrimaryKeyField, FloatField, ForeignKeyField

from Models.GroupCourse import GroupCourse
from Models.Student import Student


class ChoiceCourse(BaseModel):
    id = PrimaryKeyField()
    Student_student_number_id = ForeignKeyField(Student, backref='choice_course')
    status = EnumField(choices=["accept", "non_accept"])
    status_pay = EnumField(choices=["yes", "on"])
    score = FloatField()
    semeter = CharField(45)
    Group_Course_code_course_id = ForeignKeyField(GroupCourse, backref='choice_course')

    class Meta:
        db_table = "choice_course"
