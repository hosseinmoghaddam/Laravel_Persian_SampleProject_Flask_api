__author__ = 'hossein moghadam'
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
        choicecourses = ChoiceCourse.select().where(ChoiceCourse.Student_student_number_id == g.user.student_number)
        ls = [
            dict(
                id=choicecourse.id,
                Student_student_number=choicecourse.Student_student_number_id.student_number,
                status=choicecourse.status,
                status_pay=choicecourse.status_pay,
                score=choicecourse.score,
                semeter=choicecourse.semeter,
                Group_Course_code_course_id=[dict(
                    id=choicecourse.Group_Course_code_course_id.id,
                    group_number=choicecourse.Group_Course_code_course_id.group_number,
                    semester=choicecourse.Group_Course_code_course_id.semester,
                    guest_semester=choicecourse.Group_Course_code_course_id.guest_semester,
                    date_exam=choicecourse.Group_Course_code_course_id.date_exam,
                    time_exam=choicecourse.Group_Course_code_course_id.time_exam,
                    term=choicecourse.Group_Course_code_course_id.term,
                    capacity=choicecourse.Group_Course_code_course_id.capacity,
                    min_capacity=choicecourse.Group_Course_code_course_id.min_capacity,
                    Course_id=[dict(
                        id=choicecourse.Group_Course_code_course_id.Course_id.id,
                        presentation=choicecourse.Group_Course_code_course_id.Course_id.presentation,
                        type=choicecourse.Group_Course_code_course_id.Course_id.type,
                        status_prerequisite=choicecourse.Group_Course_code_course_id.Course_id.status_prerequisite,
                        name=choicecourse.Group_Course_code_course_id.Course_id.name,
                        unit_number=choicecourse.Group_Course_code_course_id.Course_id.unit_number,
                        price=choicecourse.Group_Course_code_course_id.Course_id.price,
                        list_prerequisite=choicecourse.Group_Course_code_course_id.Course_id.list_prerequisite,
                    )],
                    professor_id=[dict(
                        # id=choicecourse.Group_Course_code_course_id.professor_id.id,
                        firstname=choicecourse.Group_Course_code_course_id.professor_id.firstname,
                        lastname=choicecourse.Group_Course_code_course_id.professor_id.lastname,
                        # father=choicecourse.Group_Course_code_course_id.professor_id.father,
                        # sex=choicecourse.Group_Course_code_course_id.professor_id.sex,
                        # national_code=choicecourse.Group_Course_code_course_id.professor_id.national_code,
                        # birthday=choicecourse.Group_Course_code_course_id.professor_id.birthday,
                        # location_brith=choicecourse.Group_Course_code_course_id.professor_id.location_brith,
                        # phone=choicecourse.Group_Course_code_course_id.professor_id.phone,
                        # mobile=choicecourse.Group_Course_code_course_id.professor_id.mobile,
                        # password=choicecourse.Group_Course_code_course_id.professor_id.password,
                        # address=choicecourse.Group_Course_code_course_id.professor_id.address,
                        # img=choicecourse.Group_Course_code_course_id.professor_id.img,
                    )],
                    Time_Course_id=[dict(
                        id=choicecourse.Group_Course_code_course_id.Time_Course_id.id,
                        days=choicecourse.Group_Course_code_course_id.Time_Course_id.days,
                        time=choicecourse.Group_Course_code_course_id.Time_Course_id.time,
                        classes=choicecourse.Group_Course_code_course_id.Time_Course_id.classes,
                        rotatory=choicecourse.Group_Course_code_course_id.Time_Course_id.rotatory,
                        day_rotatory=choicecourse.Group_Course_code_course_id.Time_Course_id.day_rotatory,
                    )]
                )],
            ) for choicecourse in choicecourses
        ]
        return dict(courses=ls)


class Store(Resource):
    @auth2.login_required
    def post(self):
        request_json = request.get_json()
        choicecourse = ChoiceCourse()
        # choicecourse.id = request_json['id']
        choicecourse.Student_student_number_id = request_json['Student_student_number_id']
        choicecourse.status = request_json['status']
        choicecourse.status_pay = request_json['status_pay']
        choicecourse.score = request_json['score']
        choicecourse.semeter = request_json['semeter']
        choicecourse.Group_Course_code_course_id = request_json['Group_Course_code_course_id']

        return dict(
            status=choicecourse.save()
        )


class Update(Resource):
    @auth2.login_required
    def update(self):
        pass


class Delete(Resource):
    @auth2.login_required
    def delete(self):
        return dict(
            status=ChoiceCourse.delete().where(ChoiceCourse.Student_student_number_id == g.user.student_number).execute()
        )


class Destroy(Resource):
    @auth2.login_required
    def delete(self, choicecourse_id):
        try:
            choicecourse = ChoiceCourse.get(id=choicecourse_id)
        except ChoiceCourse.DoesNotExist:
            return None, 404
        choicecourse.delete_instance()
        return dict(status=True, id=choicecourse_id), 200
