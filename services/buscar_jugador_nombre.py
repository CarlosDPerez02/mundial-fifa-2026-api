from fastapi import APIRouter, HTTPException, Depends
from models.jugador_base_datos import JugadorResponse
from sqlalchemy.orm import Session
from database.dependency import get_db
from models.jugador_db import JugadorDB
from models.convertir_jugador import convertir_jugador

router = APIRouter(
        prefix="/jugadores",
        tags=["jugadores"]
)
@router.get("/nombre/{jugador_nombre}", response_model=JugadorResponse)
def buscar_jugador_nombre(
    jugador_nombre: str,
    db: Session = Depends(get_db)
):
    jugador = db.query(JugadorDB).filter(
        JugadorDB.nombre.ilike(f"{jugador_nombre}%")
    ).first()
    
    if not jugador:
        raise HTTPException(
            status_code=404,
            detail="Jugador no encontrado"
        )
    return convertir_jugador(jugador)


