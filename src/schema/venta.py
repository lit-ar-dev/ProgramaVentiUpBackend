from datetime import datetime
from typing import List
from pydantic import BaseModel
from schema.cliente import ClienteRead
from schema.detalle_de_venta import DetalleDeVentaCreate, DetalleDeVentaRead
from schema.metodo_de_pago import MetodoDePagoRead
from schema.usuario import UsuarioRead


class VentaBase(BaseModel):
    fecha: datetime

class VentaCreate(VentaBase):
    metodo_de_pago_nombre: str
    cliente_nombre: str
    cajero_nombre: str
    detalle: List[DetalleDeVentaCreate] = []
    importe_total: float

class VentaRead(VentaBase):
    id: int
    metodo_de_pago: MetodoDePagoRead
    cliente: ClienteRead
    cajero: UsuarioRead
    detalles: List[DetalleDeVentaRead] = []

    class Config:
        from_attributes = True

class VentaUpdate(VentaBase):
    metodo_de_pago_nombre: str
    cliente_nombre: str
    cajero_nombre: str
    detalle: List[DetalleDeVentaCreate] = []
    importe_total: float