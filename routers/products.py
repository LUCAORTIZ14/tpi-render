from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import get_database_session
from models.products import Productos as ProductoModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.products import ProductService
from schemas.products import Product

products_router = APIRouter()


@products_router.get('/productos', tags=['productos'], response_model=List[Product], status_code=200, dependencies=[Depends(JWTBearer())])
def get_productos(db = Depends(get_database_session)) -> List[Product]:
    #db = Session()
    result = ProductService(db).get_productos()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@products_router.get('/productos/{id}', tags=['productos'], response_model=Product)
def get_producto(id: int = Path(ge=1, le=2000), db = Depends(get_database_session)) -> Product:
    #db = Session()
    result = ProductService(db).get_producto(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@products_router.get('/productos/', tags=['productos'], response_model=List[Product])
def get_product_by_category(idCategoria: int, db = Depends(get_database_session)) -> List[Product]:
    #db = Session()
    result = ProductService(db).get_productos_by_category(idCategoria)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@products_router.post('/productos', tags=['productos'], response_model=dict, status_code=201)
def create_product(producto: Product, db = Depends(get_database_session)) -> dict:
    #db = Session()
    ProductService(db).create_producto(producto)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el producto"})


@products_router.put('/productos/{id}', tags=['productos'], response_model=dict, status_code=200)
def update_producto(id: int, producto: Product, db = Depends(get_database_session))-> dict:
    #db = Session()
    result = ProductService(db).get_producto(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    ProductService(db).update_producto(id, producto)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el producto"})


@products_router.delete('/productos/{id}', tags=['productos'], response_model=dict, status_code=200)
def delete_product(id: int, db = Depends(get_database_session))-> dict:
    #db = Session()
    result: ProductoModel = db.query(ProductoModel).filter(ProductoModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    ProductService(db).delete_producto(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el producto"})