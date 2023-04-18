from peewee import CharField
from .base_model import BaseModel

class Tag(BaseModel):
    name = CharField(unique=True)
