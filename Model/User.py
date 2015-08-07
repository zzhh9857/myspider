__author__ = 'dw'
# from core import MyBaseModel;
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


class User(MyBaseModel):
    id = IntegerField(primary_key=True, index=True)
    name = CharField(unique=True, default='');
    password = CharField(default='');
    group = CharField(default='admin');
    value = FloatField(default=0.0);


User.create(username='test', password='test');
