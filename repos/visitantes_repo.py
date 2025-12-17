from peewee import *# type: ignore
from playhouse.postgres_ext import *# type: ignore
from models.visitantes_model import VisitantesModel
from models.tickets_model import TicketsModel


class VisitantesRepo:
    @staticmethod
    def crear_visitante(nombre, email, altura, fecha_registro,  preferencias_json):
        
        try:
            if preferencias_json:
                return VisitantesModel.create(nombre=nombre, email=email, altura = altura, fecha_registro = fecha_registro, preferencias_json = preferencias_json)
            else:
                return VisitantesModel.create(nombre=nombre, email=email, altura = altura, fecha_registro = fecha_registro)
        except Exception as e:
            print(f"Error insertando al visitante: {e}")
            return None


    @staticmethod
    def Buscar_todo_visitantes():
        return list(VisitantesModel.select())

    @staticmethod
    def obtener_visitantes_con_acceso_atraccion(atraccion_id):
        query = (
            VisitantesModel
            .select()
            .join(TicketsModel)
            .where(
                (TicketsModel.atraccion_id == atraccion_id) |
                (TicketsModel.tipo_ticket == "general")
            )
            .distinct()
        )
        return list(query)
