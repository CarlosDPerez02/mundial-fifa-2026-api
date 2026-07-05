from pydantic import BaseModel, Field

class Jugador(BaseModel):
    nombre: str = Field(
        ...,
        description="Nombre del jugador"
    )
    seleccion: str = Field(
        ...,
        description="Seleccion a la que pertenece el jugador",
    )
    goles: int
    asistencias: int












