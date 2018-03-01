from flask import Flask
from flask_restful import Api
import env
from Models.BaseModel import mysql_db
from Models.Student  import Students
import routes

app = Flask(__name__)
app.secret_key = env.secret_key
app.config['SECRET_KEY'] = env.secret_key

api = Api(app)

routes.route(api)

if __name__ == '__main__':
    mysql_db.connect()

    # mysql_db.create_tables([Students])

    app.run('0.0.0.0', 5000, True)
