from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List


class Categorias(BaseModel):
    id: Optional[int] = None
    descripcion: str = Field(min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "descripcion": "Verduras de primera"
            }
        }

