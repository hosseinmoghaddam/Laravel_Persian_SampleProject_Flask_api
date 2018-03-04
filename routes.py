__author__ = 'hossein moghadam'
from Controllers import LoginController, CourseController, ChoiceCourseController


def route(api):
    api.add_resource(LoginController.Login, '/login', endpoint='login')
    api.add_resource(CourseController.List, '/courses', endpoint='course_list')
    api.add_resource(ChoiceCourseController.List, '/choice_courses', endpoint='choice_course_list')
    api.add_resource(ChoiceCourseController.Update, '/choice_courses', endpoint='update_choice_courses')
    api.add_resource(ChoiceCourseController.Delete, '/choice_courses', endpoint='delete_choice_courses')
    api.add_resource(ChoiceCourseController.Store, '/choice_courses', endpoint='create_choice_course')
    api.add_resource(ChoiceCourseController.Destroy, '/choice_courses/<int:choicecourse_id>', endpoint='delete_choice_course')

