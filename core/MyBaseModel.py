__author__ = 'dw'

from peewee import *;

db = MySQLDatabase(host="127.0.0.1", user="root", passwd="123456", database="test", charset="utf-8");

class MyBaseModel(Model):
    class Meta:
        database = db;

    @classmethod
    def getOne(cls, *query, **kwargs):
        try:
            return cls.get(*query, **kwargs)
        except DoesNotExist:
            return None;
