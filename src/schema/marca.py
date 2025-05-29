from pydantic import BaseModel


class MarcaBase(BaseModel):
    nombre: str

class MarcaCreate(MarcaBase):
    pass

class MarcaRead(MarcaBase):
    id: int

    class Config:
        from_attributes = True

class MarcaUpdate(MarcaBase):
    pass