from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependency import get_db
from models.jugador_db import JugadorDB
from models.jugador_base_datos import JugadorResponse
from models.convertir_jugador import convertir_jugador

router = APIRouter(
    prefix="/jugadores",
    tags=["/jugadores"]
)

@router.get("/", response_model=list[JugadorResponse])
def lista(db: Session = Depends(get_db)):
    jugadores = db.query(JugadorDB).all()

    return [convertir_jugador(jugador) for jugador in jugadores]