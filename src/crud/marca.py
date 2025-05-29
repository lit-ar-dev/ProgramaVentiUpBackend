from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.marca import Marca
from schema.marca import MarcaCreate, MarcaUpdate


def create_marca(db: Session, marca: MarcaCreate) -> Marca:
    try:
        db_marca = Marca(nombre=marca.nombre)
        db.add(db_marca)
        db.commit()
        db.refresh(db_marca)
        return db_marca
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def read_marcas(db: Session) -> list[Marca]:
    return db.query(Marca).all()

def read_marca_by_id(db: Session, marca_id: int) -> Marca:
    return db.query(Marca).filter(Marca.id == marca_id).first()

def read_marca_by_nombre(db: Session, nombre: str) -> Marca:
    return db.query(Marca).filter(Marca.nombre == nombre).first()

def update_marca(db: Session, marca_id: int, marca: MarcaUpdate) -> Marca:
    db_marca = read_marca_by_id(db, marca_id)
    if db_marca:
        db_marca.nombre = marca.nombre
        db.commit()
        db.refresh(db_marca)
    return db_marca

def delete_marca(db: Session, marca_id: int) -> None:
    db_marca = read_marca_by_id(db, marca_id)
    if not db_marca:
        raise ValueError("Marca no existente")
    try:
        db.delete(db_marca)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e