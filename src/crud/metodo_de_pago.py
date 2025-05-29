from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.metodo_de_pago import MetodoDePago
from schema.metodo_de_pago import MetodoDePagoCreate, MetodoDePagoUpdate


def create_metodo_de_pago(db: Session, metodo_de_pago: MetodoDePagoCreate) -> MetodoDePago:
    try:
        db_metodo_de_pago = MetodoDePago(nombre=metodo_de_pago.nombre)
        db.add(db_metodo_de_pago)
        db.commit()
        db.refresh(db_metodo_de_pago)
        return db_metodo_de_pago
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def read_metodos_de_pago(db: Session) -> list[MetodoDePago]:
    return db.query(MetodoDePago).all()

def read_metodo_de_pago_by_id(db: Session, metodo_de_pago_id: int) -> MetodoDePago | None:
    return db.query(MetodoDePago).filter(MetodoDePago.id == metodo_de_pago_id).first()

def read_metodo_de_pago_by_nombre(db: Session, nombre: str) -> MetodoDePago | None:
    return db.query(MetodoDePago).filter(MetodoDePago.nombre == nombre).first()

def update_metodo_de_pago(db: Session, metodo_de_pago_id: int, metodo_de_pago: MetodoDePagoUpdate) -> MetodoDePago | None:
    db_metodo_de_pago = read_metodo_de_pago_by_id(db, metodo_de_pago_id)
    if db_metodo_de_pago:
        db_metodo_de_pago.nombre = metodo_de_pago.nombre
        db.commit()
        db.refresh(db_metodo_de_pago)
    return db_metodo_de_pago

def delete_metodo_de_pago(db: Session, metodo_de_pago_id: int) -> None:
    db_metodo_de_pago = read_metodo_de_pago_by_id(db, metodo_de_pago_id)
    if not db_metodo_de_pago:
        raise ValueError("Método de pago no existente")
    try:
        db.delete(db_metodo_de_pago)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e