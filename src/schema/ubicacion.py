from pydantic import BaseModel


class UbicacionBase(BaseModel):
    nombre: str

class UbicacionCreate(UbicacionBase):
    pass

class UbicacionRead(UbicacionBase):
    id: int

    class Config:
        from_attributes = True

class UbicacionUpdate(UbicacionBase):
    pass