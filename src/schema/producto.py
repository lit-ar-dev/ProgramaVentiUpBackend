from typing import Optional
from pydantic import BaseModel
from typing import Optional


class ProductoBase(BaseModel):
    codigo: str
    nombre: str
    marca_nombre: str
    descripcion: Optional[str] = None
    unidad_de_medida_nombre: str
    precio: float

class ProductoCreate(ProductoBase):
    pass

class ProductoRead(ProductoBase):
    id: int
    medida_de_venta_nombre: str

    class Config:
        from_attributes = True

class ProductoUpdate(ProductoBase):
    pass