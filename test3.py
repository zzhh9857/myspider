from peewee import *;

db = MySQLDatabase(host="127.0.0.1", user="root", passwd="123456", database="test", charset="utf-8");


class User(Model):
    name = CharField(unique=True, default='');
    password = CharField(default='');
    group = CharField(default='admin');
    value = FloatField(default=0.0);


User.create_table();
