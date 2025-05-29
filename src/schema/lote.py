from pydantic import BaseModel
from datetime import date
from schema.producto import ProductoRead


class LoteBase(BaseModel):
    codigo_de_lote: str
    existencia: float
    fecha_de_vencimiento: date
    estado_de_lote_nombre: str
    ubicacion_nombre: str

class LoteCreate(LoteBase):
    codigo_de_producto: str

class LoteRead(LoteBase):
    id: int
    producto: ProductoRead

    class Config:
        from_attributes = True

class LoteUpdate(LoteBase):
    codigo_de_producto: str
