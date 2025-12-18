

from database import db
from repos.visitantes_repo import VisitantesRepo
from repos.atracciones_repo import AtraccionesRepo
from repos.tickets_repo import TicketsRepo
import consultas


#Menu Princupal de uso de la aplicacion
visitantes_repo = VisitantesRepo()
atracciones_repo = AtraccionesRepo()
tickets_repo = TicketsRepo()

#Metodos de creacion del menu
def menu_principal():
    print("\n=== MENU BASE DE DATOS ===")
    print("1. Gestion de Visitantes")
    print("2. Gestion de Atracciones")
    print("3. Gestion de Tickets")
    print("4. Consultas")
    print("0. Salir")
    return input("Selecciona una opcion: ")


def menu_visitantes():
    print("\n--- VISITANTES ---")
    print("1. Listar visitantes")
    print("2. Crear visitante")
    print("3. Eliminar visitante")
    print("0. Volver")
    return input("Opcion: ")


def menu_atracciones():
    print("\n--- ATRACCIONES ---")
    print("1. Listar atracciones")
    print("2. Crear atraccion")
    print("3. Eliminar atraccion")
    print("0. Volver")
    return input("Opcion: ")


def menu_tickets():
    print("\n--- TICKETS ---")
    print("1. Listar tickets")
    print("2. Crear ticket")
    print("3. Eliminar ticket")
    print("0. Volver")
    return input("Opcion: ")


def menu_consultas():
    print("\n--- CONSULTAS ---")
    print("1. Visitantes con preferencia extrema")
    print("2. Atracciones con intensidad > 7")
    print("3. Tickets de colegio < 30€")
    print("4. Atracciones con duracion larga")
    print("5. Visitantes con problemas cardiacos")
    print("0. Volver")
    return input("Opcion: ")

#Metodo final de uso del menu
def main():
    db.connect(reuse_if_open=True)

    while True:
        
        opcion = menu_principal()

        if opcion == "1":
            op = menu_visitantes()
            if op == "1":
                for v in visitantes_repo.get_all():
                    print(v)
            elif op == "2":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                visitantes_repo.create(nombre=nombre, edad=edad)
            elif op == "3":
                id_v = int(input("ID visitante: "))
                visitantes_repo.delete(id_v)

        elif opcion == "2":
            op = menu_atracciones()
            if op == "1":
                for a in atracciones_repo.get_all():
                    print(a)
            elif op == "2":
                nombre = input("Nombre: ")
                atracciones_repo.create(nombre=nombre)
            elif op == "3":
                id_a = int(input("ID atraccion: "))
                atracciones_repo.delete(id_a)

        elif opcion == "3":
            op = menu_tickets()
            if op == "1":
                for t in tickets_repo.get_all():
                    print(t)
            elif op == "2":
                tipo = input("Tipo ticket: ")
                tickets_repo.create(tipo_ticket=tipo)
            elif op == "3":
                id_t = int(input("ID ticket: "))
                tickets_repo.delete(id_t)

        elif opcion == "4":
            op = menu_consultas()
            if op == "1":
                for r in consultas.visitantes_preferencia_extrema():
                    print(r)
            elif op == "2":
                for r in consultas.atracciones_intensidad_mayor_7():
                    print(r)
            elif op == "3":
                for r in consultas.tickets_colegio_menos_30():
                    print(r)
            elif op == "4":
                for r in consultas.atracciones_duracion_larga():
                    print(r)
            elif op == "5":
                for r in consultas.visitantes_con_problemas_cardiacos():
                    print(r)

        elif opcion == "0":
            break

    db.close()


if __name__ == "__main__":
    main()
