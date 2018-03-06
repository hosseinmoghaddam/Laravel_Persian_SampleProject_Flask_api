from passlib.handlers.bcrypt import bcrypt

from Models.Professor import Professor

__author__ = 'hossein moghadam'


def professor_seed():
    professor = Professor()
    professor.firstname = 'حسین'
    professor.lastname = 'مقدم'
    professor.father = 'فرزاد'
    professor.sex = 'male'
    professor.national_code = '1234'
    professor.birthday = '1374-09-20'
    professor.location_brith = 'طهران'
    professor.phone = '09380934231'
    professor.mobile = '026152482'
    professor.password = bcrypt.hash('1234')
    professor.address = 'قاین میدان شیرازی'
    professor.img = 'ندارد'
    professor.save()

    professor = Professor()
    professor.firstname = 'علی'
    professor.lastname = 'احمدی'
    professor.father = 'فرزاد'
    professor.sex = 'male'
    professor.national_code = '4321'
    professor.birthday = '1374-02-20'
    professor.location_brith = 'طهران'
    professor.phone = '09380125486'
    professor.mobile = '02615452482'
    professor.password = bcrypt.hash('1234')
    professor.address = 'قاین میدان شیرازی'
    professor.img = 'ندارد'
    professor.save()

    print('create all Professors successfully')

