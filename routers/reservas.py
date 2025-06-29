from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import get_database_session
from models.reservas import Reserva as ReservaModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.reservas import ReservaService
from schemas.reservas import Reserva

reservas_router = APIRouter()


@reservas_router.get('/Reserva', tags=['Reserva'], response_model=List[Reserva], status_code=200, dependencies=[Depends(JWTBearer())])
def get_reservas(db = Depends(get_database_session)) -> List[Reserva]:
    #db = Session()
    result = ReservaService(db).get_vReserva()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@reservas_router.get('/Reserva/{id}', tags=['Reserva'], response_model=Reserva)
def get_reserva(id: int = Path(ge=1, le=2000), db = Depends(get_database_session)) -> Reserva:
    #db = Session()
    result = ReservaService(db).get_Reserva(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@reservas_router.get('/Reserva/', tags=['Reserva'], response_model=List[Reserva])
def get_usuarios_by_estado(estado: str = Query(min_length=1, max_length=50), db = Depends(get_database_session) ) -> List[Reserva]:
    #db = Session()
    result = ReservaService(db).get_Reserva_by_estado(estado)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@reservas_router.post('/Reserva', tags=['Reserva'], response_model=dict, status_code=201)
def create_reservas(reserva: Reserva, db = Depends(get_database_session)) -> dict:
    #db = Session()
    ReservaService(db).create_Reserva(reserva)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la reserva"})

@reservas_router.delete('/Reserva/{id}', tags=['Reserva'], response_model=dict, status_code=200)
def delete_reservas(id: int, db = Depends(get_database_session))-> dict:
    #db = Session()
    result: ReservaModel = db.query(ReservaModel).filter(ReservaModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    ReservaService(db).delete_Reserva(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la reserva"})