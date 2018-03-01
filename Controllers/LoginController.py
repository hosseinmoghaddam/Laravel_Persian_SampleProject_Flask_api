from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import session, url_for, request, redirect, g
from Models.Student import Students
from Middleware.Auth import auth


class Login(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token(600)
        return {'token': token.decode('ascii'), 'duration': 600}

    @auth.login_required
    def post(self):
        token = g.user.generate_auth_token(600)
        return {'token': token.decode('ascii'), 'duration': 600}
