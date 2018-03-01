from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from Models.Student import Students

auth = HTTPBasicAuth()
auth2 = HTTPTokenAuth()


# noinspection PyBroadException
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = Students.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        try:
            user = Students.get(Students.student_number == username_or_token)
        except:
            user = None
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@auth2.verify_token
def verify_token(token):
    user = Students.verify_auth_token(token)
    if user:
        g.user = user
        return True
    return False

# class Auth:
#
#     def hash_password(Student, password):
#         Student.password = pwd_context.encrypt(password)
#
#     def verify_password(self, password):
#         return pwd_context.verify(password, Student.password)
#
#     def generate_auth_token(self, expiration=600):
#         s = Serializer(env.secret_key, expires_in=expiration)
#         return s.dumps({'student_number': Student.student_number})
#
#     @staticmethod
#     def verify_auth_token(token):
#         s = Serializer(env.secret_key)
#         try:
#             data = s.loads(token)
#         except SignatureExpired:
#             return None  # valid token, but expired
#         except BadSignature:
#             return None  # invalid token
#         try:
#             user = Student.get(Student.student_number == data['student_number'])
#             return user
#         except:
#             return None
