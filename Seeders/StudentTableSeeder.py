from passlib.handlers.bcrypt import bcrypt

from Models.Student import Student

__author__ = 'hossein moghadam'


def student_seed():
    successful = 0

    student = Student()
    student.firstname = 'حسین'
    student.lastname = 'مقدم'
    student.father = 'فرزاد'
    student.brithday = '1374-09-20'
    student.location_brith = 'طهران'
    student.phone = '0938094831'
    student.mobile = '02623588'
    student.national_code = '1234'
    student.status = 'active'
    student.entry_semester = '1396-تیر'
    student.img = 'ندارد'
    student.address = 'قاین'
    student.student_number = 3963001
    student.id = 1
    student.password = bcrypt.hash('1234')
    successful = successful + 1 if student.save() else successful

    student = Student()
    student.firstname = 'علی'
    student.lastname = 'یداللهی'
    student.father = 'عظاالدین'
    student.brithday = '1374-09-23'
    student.location_brith = 'طهران'
    student.phone = '09137304084'
    student.mobile = '02623588'
    student.national_code = '4321'
    student.status = 'active'
    student.entry_semester = '1396-تیر'
    student.img = 'ندارد'
    student.address = 'اصفهان'
    student.student_number = 3963002
    student.id = 2
    student.password = bcrypt.hash('1234')
    successful = successful + 1 if student.save() else successful

    print(str(successful)+' Students created successfully')
