from fastapi import APIRouter,HTTPException
from models.jugador import Jugador
from models.jugador_base_datos import JugadorResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from database.dependency import get_db
from models.jugador_db import JugadorDB
from models.selecciones_db import SeleccionesDB
from models.convertir_jugador import convertir_jugador

router = APIRouter(
    prefix="/jugadores",
    tags=["/jugadores"]
)

@router.post("/", response_model=JugadorResponse)
def registrar_jugadores(jugador: Jugador, db: Session = Depends(get_db)):
    
    
    consulta_sele = db.query(SeleccionesDB).filter(
        SeleccionesDB.seleccion == jugador.seleccion
    ).first()
    
    if not consulta_sele:
        raise HTTPException(
            status_code=404,
            detail="La selección no existe")
        
    existe = db.query(JugadorDB).filter(
        JugadorDB.nombre == jugador.nombre,
        JugadorDB.seleccion_id == consulta_sele.id
    ).first()
    
    if existe:
        raise HTTPException(   
            status_code=409, 
            detail="El jugador ya esta registrado")

    nuevo_jugador = JugadorDB(
        nombre=jugador.nombre,
        seleccion_id = consulta_sele.id,
        goles=jugador.goles,
        asistencias=jugador.asistencias
    )
    db.add(nuevo_jugador)
    db.commit()
    db.refresh(nuevo_jugador)

    return convertir_jugador(nuevo_jugador)
