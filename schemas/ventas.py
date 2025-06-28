from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import date

class Ventas(BaseModel):
    id: Optional[int] = None
    idUsuario: int 
    emailUsuario: Optional[EmailStr]=None, 
    idProducto: int 
    nombreProducto:Optional[str] = None, 
    cantidad: int
    fecha: date
    despachado: bool
class VentasUpdate(BaseModel):
    despachado: bool    

   

