from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.medida_de_venta import MedidaDeVenta
from schema.medida_de_venta import MedidaDeVentaCreate


def create_medida_de_venta(db: Session, medida_de_venta: MedidaDeVentaCreate) -> MedidaDeVenta:
    try:
        db_medida_de_venta = MedidaDeVenta(nombre=medida_de_venta.nombre)
        db.add(db_medida_de_venta)
        db.commit()
        db.refresh(db_medida_de_venta)
        return db_medida_de_venta
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def read_medidas_de_venta(db: Session) -> list[MedidaDeVenta]:
    return db.query(MedidaDeVenta).all()

def read_medida_de_venta(db: Session, medida_de_venta_id: int) -> MedidaDeVenta:
    return db.query(MedidaDeVenta).filter(MedidaDeVenta.id == medida_de_venta_id).first()

def read_medida_de_venta_by_nombre(db: Session, nombre: str) -> MedidaDeVenta:
    return db.query(MedidaDeVenta).filter(MedidaDeVenta.nombre == nombre).first()