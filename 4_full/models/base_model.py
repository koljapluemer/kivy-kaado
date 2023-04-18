# Base model for ORM models

from peewee import Model, SqliteDatabase

db = SqliteDatabase("app.db")

class BaseModel(Model):
    class Meta:
        database = db