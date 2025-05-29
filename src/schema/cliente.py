from typing import Optional
from pydantic import BaseModel


class ClienteBase(BaseModel):
    nombre: str
    numero_de_telefono: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteRead(ClienteBase):
    id: int

    class Config:
        from_attributes = True

class ClienteUpdate(ClienteBase):
    pass