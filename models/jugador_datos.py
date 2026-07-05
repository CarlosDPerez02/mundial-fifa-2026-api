from pydantic import BaseModel, Field

class JugadorDatos(BaseModel):
    nombre: str | None = Field(
        default=None,
        description="Nombre del jugador",
    )
