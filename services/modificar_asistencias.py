from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.dependency import get_db
from models.jugador_db import JugadorDB
from models.jugador_asistencias import JugadorAsistencias
from models.jugador_base_datos import JugadorResponse
from models.convertir_jugador import convertir_jugador

router = APIRouter(
        prefix="/jugadores",
        tags=["jugadores"]
)
@router.put("/{jugador_id}/asistencias", response_model=JugadorResponse)
def actualizar_asistencias(jugador_id:int, updateJugadorAsis: JugadorAsistencias, db:Session = Depends(get_db)):
        jugador = db.query(JugadorDB).filter(
                JugadorDB.id == jugador_id
        ).first() 
        
        if not jugador:
                raise HTTPException(
                status_code=404,
                detail="Jugador no encontrado"
        )
                
        jugador.asistencias = updateJugadorAsis.asistencias
        
        db.commit()
        db.refresh(jugador)
        
        return convertir_jugador(jugador)
