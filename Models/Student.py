from passlib.handlers.bcrypt import bcrypt

from Models.BaseModel import BaseModel
import os
from peewee import IntegerField, TextField, CharField, PrimaryKeyField
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import env


class Student(BaseModel):
    firstname = CharField()
    lastname = CharField()
    father = CharField(default='test')
    brithday = CharField(default='test')
    location_brith = CharField(default='test')
    phone = CharField(default='test')
    mobile = CharField(default='test')
    national_code = CharField(default='test')
    status = CharField(default='test')
    entry_semester = CharField(default='test')
    img = CharField(default='test')
    address = TextField(default='test')
    student_number = IntegerField(unique=True)
    id = PrimaryKeyField()
    password = CharField()

    class Meta:
        db_table = "student"
        order_by = ('student_number',)

    def hash_password(self, password):
        self.password = bcrypt.hash(password)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(env.secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(env.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        try:
            user = Student.get(Student.id == data['id'])
            return user
        except:
            return None


if __name__ == '__main__':
    u = Student()
    u.firstname = 'hossein'
    u.lastname = 'moghadam'
    u.address = 'tehran'
    u.student_number = 123
    u.hash_password("123")
    u.save()
