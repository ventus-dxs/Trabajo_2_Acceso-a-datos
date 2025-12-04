from peewee import * # type: ignore
from database import db # type: ignore


class BaseModel(Model):
    class Meta:
        database = db