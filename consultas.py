from peewee import fn, JOIN
from models.visitantes_model import Visitante
from models.atracciones_model import Atraccion
from models.tickets_model import Ticket

# ============================
# CONSULTAS BASICAS (2.5 puntos)
# ============================

def visitantes_preferencia_extrema():
    return Visitante.select().where(
        Visitante.preferencias['tipo_favorito'] == 'extrema'
    )

def atracciones_intensidad_mayor_7():
    return Atraccion.select().where(
        Atraccion.detalles['intensidad'] > 7
    )

def tickets_colegio_menos_30():
    return Ticket.select().where(
        (Ticket.tipo_ticket == 'colegio') &
        (Ticket.detalles_compra['precio'] < 30)
    )

def atracciones_duracion_larga():
    return Atraccion.select().where(
        Atraccion.detalles['duracion_segundos'] > 120
    )

def visitantes_con_problemas_cardiacos():
    return Visitante.select().where(
        Visitante.preferencias['restricciones'].contains(['problemas_cardiacos'])
    )

def atracciones_looping_y_caida():
    return Atraccion.select().where(
        Atraccion.detalles['caracteristicas'].contains(['looping']) &
        Atraccion.detalles['caracteristicas'].contains(['caida_libre'])
    )

def tickets_con_descuento_estudiante():
    return Ticket.select().where(
        Ticket.detalles_compra['descuentos_aplicados'].contains(['estudiante'])
    )

def atracciones_con_mantenimiento():
    return Atraccion.select().where(
        Atraccion.detalles['horarios']['mantenimiento'].is_null(False)
    )

# ============================
# MODIFICACIONES JSONB (2 puntos)
# ============================

def cambiar_precio_ticket(ticket_id, nuevo_precio):
    t = Ticket.get_by_id(ticket_id)
    datos = t.detalles_compra
    datos['precio'] = nuevo_precio
    t.detalles_compra = datos
    t.save()

def eliminar_restriccion_visitante(visitante_id, restriccion):
    v = Visitante.get_by_id(visitante_id)
    prefs = v.preferencias

    if restriccion in prefs['restricciones']:
        prefs['restricciones'].remove(restriccion)

    v.preferencias = prefs
    v.save()

def anadir_caracteristica_atraccion(atraccion_id, caracteristica):
    a = Atraccion.get_by_id(atraccion_id)
    det = a.detalles
    det['caracteristicas'].append(caracteristica)
    a.detalles = det
    a.save()

def anadir_visita_historial(visitante_id, visita):
    v = Visitante.get_by_id(visitante_id)
    prefs = v.preferencias
    prefs['historial_visitas'].append(visita)
    v.preferencias = prefs
    v.save()

# ============================
# CONSULTAS UTILES (3 puntos)
# ============================

def visitantes_ordenados_por_tickets():
    return (Visitante
            .select(Visitante, fn.COUNT(Ticket.id).alias('total'))
            .join(Ticket, JOIN.LEFT_OUTER)
            .group_by(Visitante)
            .order_by(fn.COUNT(Ticket.id).desc()))

def top_5_atracciones():
    return (Atraccion
            .select(Atraccion, fn.COUNT(Ticket.id).alias('ventas'))
            .join(Ticket, JOIN.LEFT_OUTER)
            .where(Ticket.atraccion_id.is_null(False))
            .group_by(Atraccion)
            .order_by(fn.COUNT(Ticket.id).desc())
            .limit(5))

def visitantes_gasto_mayor_100():
    return (Visitante
            .select(Visitante, fn.SUM(Ticket.detalles_compra['precio']).alias('gasto'))
            .join(Ticket)
            .group_by(Visitante)
            .having(fn.SUM(Ticket.detalles_compra['precio']) > 100))

def atracciones_compatibles(visitante_id):
    v = Visitante.get_by_id(visitante_id)

    return Atraccion.select().where(
        (Atraccion.activa == True) &
        (Atraccion.tipo == v.preferencias['tipo_favorito']) &
        (Atraccion.altura_minima <= v.altura)
    )