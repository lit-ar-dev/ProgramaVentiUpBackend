from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.ubicacion import Ubicacion
from schema.ubicacion import UbicacionCreate, UbicacionUpdate


def create_ubicacion(db: Session, ubicacion: UbicacionCreate) -> Ubicacion:
    try:
        db_ubicacion = Ubicacion(nombre=ubicacion.nombre)
        db.add(db_ubicacion)
        db.commit()
        db.refresh(db_ubicacion)
        return db_ubicacion
    except (SQLAlchemyError, ValueError):
        db.rollback()
        raise

def read_ubicaciones(db: Session) -> list[Ubicacion]:
    return db.query(Ubicacion).all()

def read_ubicacion_by_id(db: Session, ubicacion_id: int) -> Ubicacion | None:
    return db.query(Ubicacion).filter(Ubicacion.id == ubicacion_id).first()

def read_ubicacion_by_nombre(db: Session, nombre: str) -> Ubicacion | None:
    return db.query(Ubicacion).filter(Ubicacion.nombre == nombre).first()

def update_ubicacion(db: Session, ubicacion_id: int, ubicacion: UbicacionUpdate) -> Ubicacion | None:
    db_ubicacion = read_ubicacion_by_id(db, ubicacion_id)
    if db_ubicacion:
        db_ubicacion.nombre = ubicacion.nombre
        db.commit()
        db.refresh(db_ubicacion)
    return db_ubicacion

def delete_ubicacion(db: Session, ubicacion_id: int) -> None:
    db_ubicacion = read_ubicacion_by_id(db, ubicacion_id)
    if not db_ubicacion:
        raise ValueError("Ubicación no existente")
    try:
        db.delete(db_ubicacion)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e