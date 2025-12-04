from models.basemodel import BaseModel
from peewee import *# type: ignore
from playhouse.postgres_ext import *# type: ignore
from datetime import datetime


class Atracciones(BaseModel):
    id = AutoField()

    nombre = CharField(unique=True, null=False)
    tipo = CharField()  # extrema, familiar, infantil, acuatica
    altura_minima = IntegerField()  # en cm

    preferencias = BinaryJSONField(null=True, default={# type: ignore
    
    "duracion_segundos": 60,
    "capacidad_por_turno": 24,
    "intensidad": 8,
    "caracteristicas": ["looping", "caida_libre", "giro_360"],
    "horarios": {
        "apertura": "10:00",
        "cierre": "22:00",
        "mantenimiento": ["14:00-15:00"]
        }
    })

    activa = BooleanField(default=True)
    fecha_inauguracion = DateField(default=date.today) #type: ignore