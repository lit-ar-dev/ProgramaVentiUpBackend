from pydantic import BaseModel


class MedidaDeVentaBase(BaseModel):
    nombre: str

class MedidaDeVentaCreate(MedidaDeVentaBase):
    pass

class MedidaDeVentaRead(MedidaDeVentaBase):
    id: int

    class Config:
        from_attributes = True

class MedidaDeVentaUpdate(MedidaDeVentaBase):
    pass