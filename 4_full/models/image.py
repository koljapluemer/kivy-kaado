# Image model
from peewee import CharField, ForeignKeyField
from .base_model import BaseModel
from .card import Card

class Image(BaseModel):
    file_path = CharField()
    card = ForeignKeyField(Card, backref='images')
