from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.dependency import get_db
from models.jugador_db import JugadorDB

router = APIRouter(
    prefix="/jugadores",
    tags=["jugadores"]
)

@router.delete("/{jugador_id}")
def eliminar_jugador(
    jugador_id: int,
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
    db.delete(jugador)
    db.commit()
    
    return {"respuesta": "Jugador eliminado correctamente"}

