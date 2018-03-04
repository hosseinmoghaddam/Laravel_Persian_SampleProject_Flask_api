from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import session, url_for, request, redirect, g

from Models.Course import Course
from Models.Student import Student
from Middleware.Auth import auth2


class List(Resource):
    @auth2.login_required
    def get(self):
        res = Course.select()
        ls = [
            dict(
                id=course.id,
                presentation=course.presentation,
                type=course.type,
                status_prerequisite=course.status_prerequisite,
                name=course.name,
                unit_number=course.unit_number,
                price=course.price,
                list_prerequisite=course.list_prerequisite
            ) for course in res
        ]
        return dict(courses=ls)
