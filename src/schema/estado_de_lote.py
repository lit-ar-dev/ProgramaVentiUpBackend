from pydantic import BaseModel


class EstadoDeLoteBase(BaseModel):
    nombre: str

class EstadoDeLoteCreate(EstadoDeLoteBase):
    pass

class EstadoDeLoteRead(EstadoDeLoteBase):
    id: int

    class Config:
        from_attributes = True

class EstadoDeLoteUpdate(EstadoDeLoteBase):
    pass
