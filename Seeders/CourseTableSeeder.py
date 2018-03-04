__author__ = 'hossein moghadam'
from Models.Course import Course


def course_seed():
    course = Course()
    course.name = "پیاده سازی پایگاه داده"
    course.presentation = "practical"
    course.type = "public"
    course.status_prerequisite = "yes"
    course.price = 6000
    course.list_prerequisite = ""
    course.unit_number = 2
    course.save()

    course2 = Course()
    course2.name = "پروژه تخصصی"
    course2.presentation = "practical"
    course2.type = "public"
    course2.status_prerequisite = "yes"
    course2.price = 1000
    course2.list_prerequisite = ""
    course2.unit_number = 2
    course2.save()

    course2 = Course()
    course2.name = "تحیلی طراحی"
    course2.presentation = "practical"
    course2.type = "public"
    course2.status_prerequisite = "yes"
    course2.price = 1000
    course2.list_prerequisite = ""
    course2.unit_number = 2
    course2.save()
