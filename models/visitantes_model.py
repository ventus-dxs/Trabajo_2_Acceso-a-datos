from models.basemodel import BaseModel
from peewee import *# type: ignore
from playhouse.postgres_ext import *# type: ignore
from datetime import datetime


class UserModel(BaseModel):
    nombre = CharField(null=False)
    email = CharField(unique=True)
    altura = int
    fecha_registro = datetime
    preferencias = BinaryJSONField(null=True, default={# type: ignore
    
        "tipo_favorito": "extrema",
        "restricciones": ["problemas_cardiacos"],
        "historial_visitas": [{"fecha": "2024-06-15", "atracciones_visitadas": 8},
                            {"fecha": "2024-08-20", "atracciones_visitadas": 12}
                            ]
    
    })
