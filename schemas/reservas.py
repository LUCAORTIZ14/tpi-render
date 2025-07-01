from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Reserva(BaseModel):
    id: Optional[int] = None
    vehiculo_id: int
    usuario_id: int
    fecha_reserva: datetime
    fecha_devolucion: datetime

    class Config:
        from_attributes = True  # Para usar .from_orm()
