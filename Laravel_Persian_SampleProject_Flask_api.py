from flask import Flask, jsonify, make_response, json
from flask_httpauth import HTTPBasicAuth
from flask.ext.mysql import MySQL


mysql = MySQL()

auth = HTTPBasicAuth()

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'qurandb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()


def user_found(username):
    cursor.execute('select student_number, password, firstname from student WHERE student_number=%s', username)
    data = cursor.fetchall()
    print(data)
    if len(data) is 0:
        return 'test'
    return data


@auth.get_password
def get_password(username):
    if username == str(user_found(username)[0][0]):
        return '1234'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/')
def home():
    dict = {
        'version': '1',
        'name': 'sample project',
    }
    return jsonify(dict)


@app.route('/student/login')
@auth.login_required
def login():
    dict = {'api': user_found('3963002')}
    return jsonify(dict)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
