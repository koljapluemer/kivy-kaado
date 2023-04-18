from peewee import CharField, TextField, BooleanField, ForeignKeyField, IntegerField, ManyToManyField
from .base_model import BaseModel
from .tag import Tag

class Card(BaseModel):
    front = TextField()
    back = TextField()
    type = CharField()
    is_active = BooleanField(default=True)
    is_priority = BooleanField(default=False)
    is_started = BooleanField(default=False)
    interval = IntegerField(default=0)
    interval_unit = CharField(choices=[('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')], default='days')
    tags = ManyToManyField(Tag, backref='cards')
