from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import session, url_for, request, redirect, g
from pyramid.tests.test_predicates import predicate

from Models.ChoiceCourse import ChoiceCourse
from Models.Course import Course
from Models.GroupCourse import GroupCourse
from Models.Student import Student
from Middleware.Auth import auth2
from Models.BaseModel import mysql_db


class List(Resource):
    @auth2.login_required
    def get(self):
        cursor = mysql_db.execute_sql(
            'SELECT name,presentation,type,status_prerequisite,unit_number,price,list_prerequisite FROM student '
            'INNER JOIN choice_course c2 ON student.student_number = c2.Student_student_number '
            'INNER JOIN group_course g ON c2.Group_Course_code_course = g.code_course '
            'INNER JOIN course c ON g.Course_id = c.id WHERE student.student_number = 3963001')
        ls = [
            dict(
                name=course[0],
                presentation=course[1],
                type=course[2],
                status_prerequisite=course[3],
                unit_number=course[4],
                price=course[5],
                list_prerequisite=course[6],
            ) for course in cursor.fetchall()
        ]
        return dict(courses=ls)


class Store(Resource):
    @auth2.login_required
    def post(self):
        pass


class Update(Resource):
    @auth2.login_required
    def update(self):
        pass


class Delete(Resource):
    @auth2.login_required
    def delete(self):
        pass


class Destroy(Resource):
    @auth2.login_required
    def delete(self):
        pass
