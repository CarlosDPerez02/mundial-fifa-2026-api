from fastapi import APIRouter, HTTPException, Depends
from models.jugador_goles import JugadorGoles
from models.jugador_goles import JugadorGoles
from sqlalchemy.orm import Session
from database.dependency import get_db
from models.jugador_db import JugadorDB
from models.jugador_base_datos import JugadorResponse
from models.convertir_jugador import convertir_jugador

router = APIRouter(
        prefix="/jugadores",
        tags=["jugadores"]
)
@router.put("/{jugador_id}/goles", response_model=JugadorResponse)
def actualizar_goles(jugador_id: int, updateJugadorGoles: JugadorGoles, db:Session = Depends(get_db)):
        jugador = db.query(JugadorDB).filter(
                JugadorDB.id == jugador_id
        ).first() 
        
        if not jugador:
                raise HTTPException(
                        status_code=404,
                        detail="Jugador no encontrado"
                )
        jugador.goles = updateJugadorGoles.goles

        db.commit()
        db.refresh(jugador)
        
        return convertir_jugador(jugador)
        

