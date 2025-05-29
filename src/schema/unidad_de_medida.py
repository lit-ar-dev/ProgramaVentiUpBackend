from pydantic import BaseModel


class UnidadDeMedidaBase(BaseModel):
    nombre: str
    descripcion: str
    medida_de_venta_nombre: str

class UnidadDeMedidaCreate(UnidadDeMedidaBase):
    pass

class UnidadDeMedidaRead(UnidadDeMedidaBase):
    id: int

    class Config:
        from_attributes = True

class UnidadDeMedidaUpdate(UnidadDeMedidaBase):
    pass