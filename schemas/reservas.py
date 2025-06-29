from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class Reserva(BaseModel):
    id: Optional[int] = None
    vehiculo_id : int
    usuario_id: int 
    fecha_reserva : datetime
    fecha_devolucion : datetime

