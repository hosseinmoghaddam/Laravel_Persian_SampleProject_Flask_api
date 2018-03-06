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

    course = Course()
    course.name = "مهندسی نرم افزار 2"
    course.presentation = "practical"
    course.type = "public"
    course.status_prerequisite = "yes"
    course.price = 8000
    course.list_prerequisite = ""
    course.unit_number = 2
    course.save()

    course = Course()
    course.name = "ریاضیات مهندسی"
    course.presentation = "practical"
    course.type = "public"
    course.status_prerequisite = "yes"
    course.price = 30000
    course.list_prerequisite = ""
    course.unit_number = 2
    course.save()

    course = Course()
    course.name = "سیگنال ها و سیستم ها"
    course.presentation = "practical"
    course.type = "public"
    course.status_prerequisite = "yes"
    course.price = 6000
    course.list_prerequisite = ""
    course.unit_number = 2
    course.save()

    course = Course()
    course.name = "آمار واحتمالات مهندسی"
    course.presentation = "practical"
    course.type = "public"
    course.status_prerequisite = "yes"
    course.price = 6000
    course.list_prerequisite = ""
    course.unit_number = 2
    course.save()

    print('create successfully all Courses')
