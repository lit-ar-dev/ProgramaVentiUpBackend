from pydantic import BaseModel


class MetodoDePagoBase(BaseModel):
    nombre: str

class MetodoDePagoCreate(MetodoDePagoBase):
    pass

class MetodoDePagoRead(MetodoDePagoBase):
    id: int

    class Config:
        from_attributes = True

class MetodoDePagoUpdate(MetodoDePagoBase):
    pass
