from services.api_router import router
from fastapi import FastAPI
import uvicorn

from services.modificacion import router as modificacion_router
from services.buscar_jugador_id import router as buscar_jugador_router
from services.eliminar import router as eliminar_router
from services.registro import router as registro_router
from services.modificar_goles import router as modificar_goles_router
from services.modificar_asistencias import router as modificar_asistencias_router
from services.lista_goles import router as goleadores_router
from services.lista_partipaciones import router as participaciones_router
from services.buscar_jugador_nombre import router as buscar_nombre_router
from services.modificar_selec import router as modificar_seleccion_router

from database.db import engine, Base
import models.jugador_db
import models.selecciones_db

from services.api_router import router
from fastapi import FastAPI
import uvicorn

from services.modificacion import router as modificacion_router
from services.buscar_jugador_id import router as buscar_jugador_router
from services.eliminar import router as eliminar_router
from services.registro import router as registro_router
from services.modificar_goles import router as modificar_goles_router
from services.modificar_asistencias import router as modificar_asistencias_router
from services.lista_goles import router as goleadores_router
from services.lista_partipaciones import router as participaciones_router
from services.buscar_jugador_nombre import router as buscar_nombre_router
from services.modificar_selec import router as modificar_seleccion_router

from database.db import engine, Base
import models.jugador_db
import models.selecciones_db

app = FastAPI(
    title="MUNDIAL FIFA 2026 API",
    description="""
API REST desarrollada con FastAPI para la gestión de jugadores del Mundial FIFA 2026.

Características:
- Registro de jugadores
- Consulta por ID y nombre
- Actualización de datos
- Gestión de goles y asistencias
- Gestión de selecciones
- Eliminación de jugadores
""",
    version="1.0.0",
    contact={
        "name": "Carlos Pérez",
        "url": "https://github.com/CarlosDPerez02/mundial-fifa-2026-api",
    },
)

app.include_router(router)
app.include_router(modificacion_router)
app.include_router(buscar_jugador_router)
app.include_router(eliminar_router)
app.include_router(registro_router)
app.include_router(modificar_goles_router)
app.include_router(modificar_asistencias_router)
app.include_router(goleadores_router)
app.include_router(participaciones_router)
app.include_router(buscar_nombre_router)
app.include_router(modificar_seleccion_router)

if __name__=="__main__": 
    uvicorn.run("main:app",port=8000,reload=True)

Base.metadata.create_all(bind=engine)