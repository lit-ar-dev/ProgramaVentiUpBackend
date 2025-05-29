from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nombre: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioRead(UsuarioBase):
    id: int

    class Config:
        from_attributes = True

class UsuarioUpdate(UsuarioBase):
    pass
