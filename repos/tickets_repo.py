from peewee import *# type: ignore
from playhouse.postgres_ext import *# type: ignore
from models.tickets_model import TicketsModel
from models.visitantes_model import VisitantesModel


class TicketsRepo:
    @staticmethod
    def crear_ticket(visitante_id, fecha_visita, tipo_ticket, detalles_compra_json, atraccion_id):

        try:
            if detalles_compra_json:
                return TicketsModel.create(visitante_id = visitante_id, fecha_visita = fecha_visita, tipo_ticket = tipo_ticket, detalles_compra_json = detalles_compra_json, atraccion_id = atraccion_id)
            else:
                return TicketsModel.create(visitante_id = visitante_id, fecha_visita = fecha_visita, tipo_ticket = tipo_ticket, atraccion_id = atraccion_id)
        except Exception as e:
            print(f"Error insertando el ticket: {e}")
            return None
        
    
    @staticmethod
    def Buscar_todo_tickets():
        return list(TicketsModel.select())
    
    @staticmethod
    def obtener_tickets_por_visitante(visitante_id):
        return list(
            TicketsModel
            .select()
            .where(TicketsModel.visitante_id == visitante_id)
        )

    @staticmethod
    def obtener_tickets_por_atraccion(atraccion_id):
        return list(
            TicketsModel
            .select()
            .where(TicketsModel.atraccion_id == atraccion_id)
        )

