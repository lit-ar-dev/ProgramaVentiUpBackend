from pydantic import BaseModel
from typing import Optional
from datetime import date

class PrecioBase(BaseModel):
    precio: float
    fecha_de_inicio: date
    fecha_de_fin: Optional[date] = None
    codigo_de_producto: str

class PrecioCreate(PrecioBase):
    pass

class PrecioRead(PrecioBase):
    id: int

    class Config:
        from_attributes = True

class PrecioUpdate(PrecioBase):
    pass