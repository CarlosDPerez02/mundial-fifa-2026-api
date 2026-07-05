from pydantic import BaseModel, Field

class JugadorDatosSelec(BaseModel):
    seleccion: str | None = Field(
        default=None,
        description="Selección a la que pertenece el jugador"
    )