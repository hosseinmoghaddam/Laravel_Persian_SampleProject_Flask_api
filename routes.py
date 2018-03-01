from flask import Flask, g
from flask_restful import Api
from Controllers import LoginController
import env


def route(api):
    api.add_resource(LoginController.Login, '/login', endpoint='login')
    # api.add_resource(main.Main, '/', endpoint='index')
