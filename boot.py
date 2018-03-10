__author__ = 'hossein moghadam'
from flask import Flask
from flask_restful import Api
import env
from Models.BaseModel import mysql_db
from Models.Student import Student
import routes
import console

app = Flask(__name__)
app.secret_key = env.secret_key
app.config['SECRET_KEY'] = env.secret_key

api = Api(app)

routes.route(api)
console.cli(app)

if __name__ == '__main__':

    app.run(env.HOST, env.PORT, env.DEBUG)
