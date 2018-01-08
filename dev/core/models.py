from peewee import *


db = SqliteDatabase("test.db")


class BaseModel(Model):
	class Meta:
		database = db


class User(BaseModel):
	id = PrimaryKeyField()
	first_name = CharField()
	last_name = CharField()
	username = CharField(unique=True)
	password = CharField()


def initialize_db():
	db.connect()
	db.create_tables([User], safe=True)


def close_db():
	db.close()