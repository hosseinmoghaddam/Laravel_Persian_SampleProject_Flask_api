from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import session, url_for, request, redirect, g

from Models.Course import Courses
from Models.Student import Students
from Middleware.Auth import auth2


class List(Resource):
    @auth2.login_required
    def get(self):
        res = Courses.select()
        ls = [
            dict(
                id=Course.id,
                presentation=Course.presentation,
                type=Course.type,
                status_prerequisite=Course.status_prerequisite,
                name=Course.name,
                unit_number=Course.unit_number,
                price=Course.price,
                list_prerequisite=Course.list_prerequisite ,
            ) for Course in res
        ]
        return dict(courses=ls)
