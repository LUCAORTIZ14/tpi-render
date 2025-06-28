from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import get_database_session
from models.ventas import Ventas as VentasModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.ventas import VentasService
from schemas.ventas import Ventas, VentasUpdate

ventas_router = APIRouter()


@ventas_router.get('/ventas', tags=['Ventas'], response_model=List[Ventas], status_code=200, dependencies=[Depends(JWTBearer())])
def get_ventass(db = Depends(get_database_session)) -> List[Ventas]:
    #db = Session()
    result = VentasService(db).get_ventass()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@ventas_router.get('/ventas/{id}', tags=['Ventas'], response_model=Ventas)
def get_ventas(id: int = Path(ge=1, le=2000), db = Depends(get_database_session)) -> Ventas:
    #db = Session()
    result = VentasService(db).get_ventas(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@ventas_router.get('/ventas/', tags=['Ventas'], response_model=List[Ventas])
def get_usuarios_by_estado(estado: str = Query(min_length=1, max_length=50), db = Depends(get_database_session) ) -> List[Ventas]:
    #db = Session()
    result = VentasService(db).get_ventas_by_estado(estado)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@ventas_router.post('/ventas', tags=['Ventas'], response_model=dict, status_code=201)
def create_ventas(venta: Ventas, db = Depends(get_database_session)) -> dict:
    #db = Session()
    VentasService(db).create_ventas(venta)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la venta"})


@ventas_router.put('/ventas/{id}', tags=['Ventas'], response_model=dict, status_code=200)
def update_ventas(id: int, Ventas:  VentasUpdate, db = Depends(get_database_session))-> dict:
    #db = Session()
    result = VentasService(db).get_ventas(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    VentasService(db).update_ventas(id, Ventas)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado ela venta"})


@ventas_router.delete('/ventas/{id}', tags=['Ventas'], response_model=dict, status_code=200)
def delete_ventas(id: int, db = Depends(get_database_session))-> dict:
    #db = Session()
    result: VentasModel = db.query(VentasModel).filter(VentasModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    VentasService(db).delete_ventas(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la venta"})