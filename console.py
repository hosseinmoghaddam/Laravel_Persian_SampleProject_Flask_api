from Seeders.CourseTableSeeder import course_seed


def cli(app):
    @app.cli.command('db_seed')
    def db_seed():
        course_seed()
