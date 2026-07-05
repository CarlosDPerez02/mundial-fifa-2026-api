from fastapi import APIRouter, Depends, HTTPException
from models.jugador_datos import JugadorDatos
from sqlalchemy.orm import Session
from database.dependency import get_db
from models.jugador_db import JugadorDB
from models.jugador_base_datos import JugadorResponse
from models.convertir_jugador import convertir_jugador

router = APIRouter(
        prefix="/jugadores",
        tags=["jugadores"]
)

@router.put("/{jugador_id}/nombre", response_model=JugadorResponse)
def actualizar_nombre(
        jugador_id: int,
        updateJugadorDato: JugadorDatos,
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
        if updateJugadorDato.nombre is not None:
                jugador.nombre = updateJugadorDato.nombre
                
        db.commit()
        db.refresh(jugador)

        return convertir_jugador(jugador)