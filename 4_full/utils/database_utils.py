# Database initialization and helper functions
from peewee import SqliteDatabase
from models import Card, Tag, Image

db = SqliteDatabase("app.db")

def initialize_database():
    db.connect()
    db.create_tables([Card, Tag, Image])
