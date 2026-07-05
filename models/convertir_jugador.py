from models.jugador_base_datos import JugadorResponse
from models.jugador_db import JugadorDB

def convertir_jugador(jugador: JugadorDB) -> JugadorResponse:
    return JugadorResponse(
        id=jugador.id,
        nombre=jugador.nombre,
        seleccion=jugador.seleccion.seleccion,
        goles=jugador.goles,
        asistencias=jugador.asistencias
    )