
from Controllers import LoginController, CourseController


def route(api):
    api.add_resource(LoginController.Login, '/login', endpoint='login')
    api.add_resource(CourseController.List, '/courses', endpoint='course_list')
    # api.add_resource(main.Main, '/', endpoint='index')
