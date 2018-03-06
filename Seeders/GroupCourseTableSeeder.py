from Models.Course import Course
from Models.GroupCourse import GroupCourse
from Models.Professor import Professor
from Models.TimeCourse import TimeCourse

__author__ = 'hossein moghadam'


def groupcourse_seed():
    groupcourse = GroupCourse()
    groupcourse.group_number = 1
    groupcourse.semester = 1
    groupcourse.guest_semester = 3
    groupcourse.date_exam = '1396-03-1'
    groupcourse.time_exam = '08:00'
    groupcourse.term = 1
    groupcourse.capacity = 45
    groupcourse.min_capacity = 15
    groupcourse.Course_id = Course.select().limit(1)[0].id
    groupcourse.professor_id = Professor.select().limit(1)[0].id
    groupcourse.Time_Course_id = TimeCourse.select().limit(1)[0].id
    groupcourse.save()

    groupcourse = GroupCourse()
    groupcourse.group_number = 1
    groupcourse.semester = 1
    groupcourse.guest_semester = 3
    groupcourse.date_exam = '1396-03-2'
    groupcourse.time_exam = '11:00'
    groupcourse.term = 1
    groupcourse.capacity = 45
    groupcourse.min_capacity = 15
    groupcourse.Course_id = Course.select().offset(1)[0].id
    groupcourse.professor_id = Professor.select().offset(1)[0].id
    groupcourse.Time_Course_id = TimeCourse.select().offset(2)[0].id
    groupcourse.save()

    groupcourse = GroupCourse()
    groupcourse.group_number = 1
    groupcourse.semester = 1
    groupcourse.guest_semester = 3
    groupcourse.date_exam = '1396-03-3'
    groupcourse.time_exam = '11:00'
    groupcourse.term = 1
    groupcourse.capacity = 45
    groupcourse.min_capacity = 15
    groupcourse.Course_id = Course.select().offset(3)[0].id
    groupcourse.professor_id = Professor.select().limit(1)[0].id
    groupcourse.Time_Course_id = TimeCourse.select().offset(2)[0].id
    groupcourse.save()

    groupcourse = GroupCourse()
    groupcourse.group_number = 1
    groupcourse.semester = 1
    groupcourse.guest_semester = 3
    groupcourse.date_exam = '1396-03-5'
    groupcourse.time_exam = '11:00'
    groupcourse.term = 1
    groupcourse.capacity = 45
    groupcourse.min_capacity = 15
    groupcourse.Course_id = Course.select().offset(4)[0].id
    groupcourse.professor_id = Professor.select().limit(1)[0].id
    groupcourse.Time_Course_id = TimeCourse.select().offset(3)[0].id
    groupcourse.save()

    groupcourse = GroupCourse()
    groupcourse.group_number = 1
    groupcourse.semester = 1
    groupcourse.guest_semester = 3
    groupcourse.date_exam = '1396-03-2'
    groupcourse.time_exam = '11:00'
    groupcourse.term = 1
    groupcourse.capacity = 45
    groupcourse.min_capacity = 15
    groupcourse.Course_id = Course.select().offset(2)[0].id
    groupcourse.professor_id = Professor.select().offset(0)[0].id
    groupcourse.Time_Course_id = TimeCourse.select().offset(3)[0].id
    groupcourse.save()

    groupcourse = GroupCourse()
    groupcourse.group_number = 1
    groupcourse.semester = 1
    groupcourse.guest_semester = 3
    groupcourse.date_exam = '1396-03-8'
    groupcourse.time_exam = '11:00'
    groupcourse.term = 1
    groupcourse.capacity = 45
    groupcourse.min_capacity = 15
    groupcourse.Course_id = Course.select().offset(1)[0].id
    groupcourse.professor_id = Professor.select().offset(1)[0].id
    groupcourse.Time_Course_id = TimeCourse.select().offset(1)[0].id
    groupcourse.save()

    print('create all GroupCourses successfully')
