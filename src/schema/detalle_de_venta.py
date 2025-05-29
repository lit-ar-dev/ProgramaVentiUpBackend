from pydantic import BaseModel
from schema.lote import LoteRead
from schema.producto import ProductoRead


class DetalleDeVentaBase(BaseModel):
    precio: float
    cantidad: float

class DetalleDeVentaCreate(DetalleDeVentaBase):
    codigo_de_producto: str
    codigo_de_lote: str

class DetalleDeVentaRead(DetalleDeVentaBase):
    renglon: int
    producto: ProductoRead
    lote: LoteRead

    class Config:
        from_attributes = True

class DetalleDeVentaUpdate(DetalleDeVentaBase):
    codigo_de_producto: str
    codigo_de_lote: str
