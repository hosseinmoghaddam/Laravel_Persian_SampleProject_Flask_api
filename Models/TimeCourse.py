from Models.BaseModel import BaseModel, EnumField
from peewee import IntegerField, TextField, CharField, PrimaryKeyField


class TimeCourse(BaseModel):
    id = PrimaryKeyField()
    days = IntegerField(30)
    time = IntegerField(30)
    classes = IntegerField(30)
    rotatory = IntegerField(30)
    day_rotatory = IntegerField(30)

    class Meta:
        db_table = "time_course"
