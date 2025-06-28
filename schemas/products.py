from pydantic import BaseModel, Field
from typing import Optional, List


class Product(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=5, max_length=50)
    descripcion: str = Field(max_length=100)
    foto: str
    precio: float = Field(gt=0)
    idCategoria:int
    categoria:str = Field(min_length=1, max_length=50)

     
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Telefono Samsung",
                "descripcion": "Teléfono de gama media",
                "foto" : "str de foto",
                "precio": "150.000",
                "idCategoria": "1",
                "categoria": "Celulares"

            }
        }

