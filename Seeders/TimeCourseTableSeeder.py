from Models.TimeCourse import TimeCourse

__author__ = 'hossein moghadam'


def timecourse_seed():
    timecourse = TimeCourse()
    timecourse.days = 2
    timecourse.time = 90
    timecourse.classes = 210
    timecourse.rotatory = '1'
    timecourse.day_rotatory = 'zoj'
    timecourse.save()

    timecourse = TimeCourse()
    timecourse.days = 1
    timecourse.time = 90
    timecourse.classes = 209
    timecourse.rotatory = '1'
    timecourse.day_rotatory = 'fard'
    timecourse.save()

    timecourse = TimeCourse()
    timecourse.days = 2
    timecourse.time = 90
    timecourse.classes = 208
    timecourse.rotatory = '1'
    timecourse.day_rotatory = 'zoj'
    timecourse.save()

    timecourse = TimeCourse()
    timecourse.days = 2
    timecourse.time = 120
    timecourse.classes = 207
    timecourse.rotatory = '1'
    timecourse.day_rotatory = 'zoj'
    timecourse.save()

    print('create all TimeCourses successfully')
