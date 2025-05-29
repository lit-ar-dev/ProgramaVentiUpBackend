from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.unidad_de_medida import UnidadDeMedida
from crud.medida_de_venta import read_medida_de_venta_by_nombre
from schema.unidad_de_medida import UnidadDeMedidaCreate


def create_unidad_de_medida(db: Session, unidad_de_medida: UnidadDeMedidaCreate) -> UnidadDeMedida:
    medida_de_venta = read_medida_de_venta_by_nombre(db, unidad_de_medida.medida_de_venta_nombre)
    if not medida_de_venta:
        raise ValueError("Medida de venta no existente")

    try:
        db_unidad_de_medida = UnidadDeMedida(nombre=unidad_de_medida.nombre, descripcion=unidad_de_medida.descripcion, medida_de_venta=medida_de_venta)
        db.add(db_unidad_de_medida)
        db.commit()
        db.refresh(db_unidad_de_medida)
        return db_unidad_de_medida
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise e

def read_unidades_de_medida(db: Session):
    return db.query(UnidadDeMedida).all()

def read_unidad_de_medida_by_id(db: Session, unidad_de_medida_id: int):
    return db.query(UnidadDeMedida).filter(UnidadDeMedida.id == unidad_de_medida_id).first()

def read_unidad_de_medida_by_nombre(db: Session, nombre: str):
    return db.query(UnidadDeMedida).filter(UnidadDeMedida.nombre == nombre).first()