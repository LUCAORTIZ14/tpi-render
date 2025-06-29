from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import get_database_session
from models.vehiculos import Vehiculos as VehiculoModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.vehiculos import VehiculoService
from schemas.vehiculos import Vehiculo

vehiculo_router = APIRouter()


@vehiculo_router.get('/vehiculos', tags=['vehiculos'], response_model=List[Vehiculo], status_code=200, dependencies=[Depends(JWTBearer())])
def get_vehiculos(db = Depends(get_database_session)) -> List[Vehiculo]:
    #db = Session()
    result = VehiculoService(db).get_vehiculos()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@vehiculo_router.get('/vehiculos/{id}', tags=['vehiculos'], response_model=Vehiculo)
def get_vehiculo(id: int = Path(ge=1, le=2000), db = Depends(get_database_session)) -> Vehiculo:
    #db = Session()
    result = VehiculoService(db).get_vehiculo(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@vehiculo_router.get('/vehiculos/', tags=['vehiculos'], response_model=List[Vehiculo])
def get_vehiculo_by_category(idCategoria: int, db = Depends(get_database_session)) -> List[Vehiculo]:
    #db = Session()
    result = VehiculoService(db).get_vehiculos_by_category(idCategoria)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@vehiculo_router.post('/vehiculos', tags=['vehiculos'], response_model=dict, status_code=201)
def create_vehiculo(vehiculo: Vehiculo, db = Depends(get_database_session)) -> dict:
    #db = Session()
    VehiculoService(db).create_vehiculo(vehiculo)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el vehiculo"})


@vehiculo_router.put('/vehiculos/{id}', tags=['vehiculos'], response_model=dict, status_code=200)
def update_vehiculo(id: int, vehiculo: Vehiculo, db = Depends(get_database_session))-> dict:
    #db = Session()
    result = VehiculoService(db).get_vehiculo(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    VehiculoService(db).update_vehiculo(id, vehiculo)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el vehiculo"})


@vehiculo_router.delete('/vehiculos/{id}', tags=['vehiculos'], response_model=dict, status_code=200)
def delete_vehiculo(id: int, db = Depends(get_database_session))-> dict:
    #db = Session()
    result: VehiculoModel = db.query(VehiculoModel).filter(VehiculoModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    VehiculoService(db).delete_vehiculo(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el vehiculo"})