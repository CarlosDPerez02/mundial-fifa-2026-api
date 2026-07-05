from database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class JugadorDB(Base):
    __tablename__ = "jugadores"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    seleccion_id = Column (Integer,ForeignKey("seleccion.id"))
    goles = Column(Integer, default=0)
    asistencias = Column(Integer, default=0)

    seleccion = relationship("SeleccionesDB", back_populates="jugadores")