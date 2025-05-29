from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.usuario import Usuario
from schema.usuario import UsuarioCreate


def create_usuario(db: Session, usuario: UsuarioCreate) -> Usuario:
    try:
        db_usuario = Usuario(nombre=usuario.nombre)
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def read_usuario_by_nombre(db: Session, nombre: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.nombre == nombre).first()