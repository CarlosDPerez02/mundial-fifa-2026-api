from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.dependency import get_db
from models.jugador_selec import JugadorDatosSelec
from models.jugador_db import JugadorDB
from models.selecciones_db import SeleccionesDB
from models.jugador_base_datos import JugadorResponse
from models.convertir_jugador import convertir_jugador

router = APIRouter(
        prefix="/jugadores",
        tags=["jugadores"]
)

@router.put("/{jugador_id}/seleccion", response_model=JugadorResponse)
def actualizar_seleccion(
        jugador_id: int,
        updateJugadorDato: JugadorDatosSelec,
        db: Session = Depends(get_db)
):
        jugador = db.query(JugadorDB).filter(
        JugadorDB.id == jugador_id
        ).first()

        if not jugador:
                raise HTTPException(
                status_code=404,
                detail="Jugador no encontrado"
        )

        if updateJugadorDato.seleccion is not None:

                nueva_seleccion = db.query(SeleccionesDB).filter(
                SeleccionesDB.seleccion == updateJugadorDato.seleccion
                ).first()

        if not nueva_seleccion:
                raise HTTPException(
                status_code=404,
                detail="La selección no existe"
                )

        jugador.seleccion_id = nueva_seleccion.id

        db.commit()

        jugador = db.query(JugadorDB).filter(
                JugadorDB.id == jugador_id
        ).first()

        return convertir_jugador(jugador)