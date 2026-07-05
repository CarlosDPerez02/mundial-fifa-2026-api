from database.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class SeleccionesDB(Base):
    __tablename__ = "seleccion"
    id = Column(Integer, primary_key=True, index=True)
    seleccion = Column(String, unique=True, nullable=False)
    jugadores = relationship("JugadorDB", back_populates="seleccion")

