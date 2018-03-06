from Models.ChoiceCourse import ChoiceCourse
from Models.GroupCourse import GroupCourse
from Models.Student import Student

__author__ = 'hossein moghadam'


def choicecourse_seed():
    successful = 0

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(0)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(0)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(1)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(0)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(0)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(1)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(1)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(1)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(0)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(2)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(1)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(2)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(0)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(3)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(1)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(3)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(0)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(4)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    choicecourse = ChoiceCourse()
    choicecourse.Student_student_number_id = Student.select().offset(1)[0].student_number
    choicecourse.status = 'accept'
    choicecourse.status_pay = 'yes'
    choicecourse.score = 5.0
    choicecourse.semeter = '1'
    choicecourse.Group_Course_code_course_id = GroupCourse.select().offset(5)[0].id
    successful = successful + 1 if choicecourse.save() else successful

    print(str(successful) + ' GroupCourses created successfully')
