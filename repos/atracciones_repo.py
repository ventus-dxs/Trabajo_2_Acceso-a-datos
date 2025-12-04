from peewee import *# type: ignore
from playhouse.postgres_ext import *# type: ignore
from models.atracciones_model import AtraccionesModel


class AtraccionesRepo:
    @staticmethod
    def crear_atraccion(nombre, tipo, altura_minima, detalles_json):

        try:
            if detalles_json:
                return AtraccionesModel.create(nombre = nombre, tipo = tipo, altura_minima = altura_minima, detalles_json = detalles_json)
            else:
                return AtraccionesModel.create(nombre = nombre, tipo = tipo, altura = altura_minima)
        except Exception as e:
            print(f"Error insertando la atraccion: {e}")
            return None
        
    
    @staticmethod
    def Buscar_todo_atracciones():

            return list(AtraccionesModel.select())