#!/usr/bin/env python
# -*- coding: utf-8 -*-


from peewee import Model, MySQLDatabase
import env

__author__ = 'Moghadam'

mysql_db = MySQLDatabase(env.DB_DATABASE, user=env.DB_USERNAME, password=env.DB_PASSWORD,
                         host=env.DB_HOST, port=env.DB_PORT)


class BaseModel(Model):
    class Meta:
        database = mysql_db
