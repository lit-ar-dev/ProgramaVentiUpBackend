from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.estado_de_lote import EstadoDeLote
from schema.estado_de_lote import EstadoDeLoteCreate, EstadoDeLoteUpdate


def create_estado_de_lote(db: Session, estado_de_lote: EstadoDeLoteCreate) -> EstadoDeLote:
    try:
        db_estado_de_lote = EstadoDeLote(nombre=estado_de_lote.nombre)
        db.add(db_estado_de_lote)
        db.commit()
        db.refresh(db_estado_de_lote)
        return db_estado_de_lote
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def read_estados_de_lote(db: Session) -> list[EstadoDeLote]:
    return db.query(EstadoDeLote).all()

def read_estado_de_lote_by_id(db: Session, estado_id: int) -> EstadoDeLote | None:
    return db.query(EstadoDeLote).filter(EstadoDeLote.id == estado_id).first()

def read_estado_de_lote_by_nombre(db: Session, nombre: str) -> EstadoDeLote | None:
    return db.query(EstadoDeLote).filter(EstadoDeLote.nombre == nombre).first()

def update_estado_de_lote(db: Session, estado_id: int, estado_de_lote: EstadoDeLoteUpdate) -> EstadoDeLote | None:
    db_estado_de_lote = read_estado_de_lote_by_id(db, estado_id)
    if db_estado_de_lote:
        db_estado_de_lote.nombre = estado_de_lote.nombre
        db.commit()
        db.refresh(db_estado_de_lote)
    return db_estado_de_lote

def delete_estado_de_lote(db: Session, estado_id: int) -> None:
    db_estado_de_lote = read_estado_de_lote_by_id(db, estado_id)
    if not db_estado_de_lote:
        raise ValueError("Estado de lote no existente")
    try:
        db.delete(db_estado_de_lote)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e