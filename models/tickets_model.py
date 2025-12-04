from models.basemodel import BaseModel
from peewee import *# type: ignore
from playhouse.postgres_ext import *# type: ignore
from datetime import datetime


class Tickets(BaseModel):
    id = AutoField()

    visitante_id = ForeignKeyField(
        'models.Visitantes', 
        backref='tickets',
        on_delete='CASCADE'
    )

    atraccion_id = ForeignKeyField(
        'models.Atracciones', 
        backref='tickets',
        null=True,
        on_delete='SET NULL'
    )

    fecha_compra = DateTimeField(default=datetime.utcnow)
    fecha_visita = DateField()

    tipo_ticket = CharField()  # general, colegio, empleado

    detalles_compra = BinaryJSONField(null=True, default={# type: ignore
    "precio": 45.99,
    "descuentos_aplicados": ["estudiante", "early_bird"],
    "servicios_extra": ["fast_pass", "comida_incluida"],
    "metodo_pago": "tarjeta"
    })

    usado = BooleanField(default=False)
    fecha_uso = DateTimeField(null=True)