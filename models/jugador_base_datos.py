from pydantic import BaseModel, Field, ConfigDict


class JugadorResponse(BaseModel):
    id: int
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
    
    model_config = ConfigDict(from_attributes=True)