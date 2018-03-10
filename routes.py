__author__ = 'hossein moghadam'
from Controllers import LoginController, CourseController, ChoiceCourseController, ScheduleController


def route(api):
    api.add_resource(LoginController.Login, '/login', endpoint='login')
    api.add_resource(CourseController.List, '/courses', endpoint='course_list')
    api.add_resource(ChoiceCourseController.List, '/choicecourses', endpoint='choice_course_list')
    api.add_resource(ChoiceCourseController.Update, '/choicecourses', endpoint='update_choice_courses')
    api.add_resource(ChoiceCourseController.Delete, '/choicecourses', endpoint='delete_choice_courses')
    api.add_resource(ChoiceCourseController.Store, '/choicecourses', endpoint='create_choice_course')
    api.add_resource(ChoiceCourseController.Destroy, '/choicecourses/<int:choice_course_id>',
                     endpoint='delete_choice_course')
    api.add_resource(ScheduleController.List, '/schedule', endpoint='schedule')
