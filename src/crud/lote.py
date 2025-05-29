from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from crud.ubicacion import create_ubicacion
from models.estado_de_lote import EstadoDeLote
from models.lote import Lote
from models.producto import Producto
from models.ubicacion import Ubicacion
from schema.lote import LoteCreate, LoteUpdate
from schema.ubicacion import UbicacionCreate


def create_lote(
    db: Session,
    lote: LoteCreate
) -> Lote:
    if db.query(Lote).filter_by(codigo_de_lote=lote.codigo_de_lote).first():
        raise ValueError("El código del lote ya existe")

    producto = db.query(Producto).filter(Producto.codigo == lote.codigo_de_producto).first()
    if not producto:
        raise ValueError("Producto no existente")
        
    estado = db.query(EstadoDeLote).filter(EstadoDeLote.nombre == lote.estado_de_lote_nombre).first()
    if not estado:
        raise ValueError("Estado de lote no existente")
        
    ubicacion = db.query(Ubicacion).filter(Ubicacion.nombre == lote.ubicacion_nombre).first()
    if not ubicacion:
        ubicacion = create_ubicacion(db, UbicacionCreate(nombre=lote.ubicacion_nombre))

    if lote.existencia <= 0:
        raise ValueError("La existencia debe ser mayor que cero")

    try:
        db_lote = Lote(
            codigo_de_lote=lote.codigo_de_lote,
            existencia=lote.existencia,
            fecha_de_vencimiento=lote.fecha_de_vencimiento,
            producto=producto,
            estado=estado,
            ubicacion=ubicacion
        )
        db.add(db_lote)
        db.commit()
        db.refresh(db_lote)
        return db_lote
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def read_lotes(db: Session) -> list[Lote]:
    return db.query(Lote).all()

def read_lote_by_id(db: Session, lote_id: int) -> Lote | None:
    return db.query(Lote).filter(Lote.id == lote_id).first()

def update_lote(
    db: Session,
    lote_id: int,
    lote: LoteUpdate
) -> Lote | None:
    db_lote = read_lote_by_id(db, lote_id)
    if not db_lote:
        raise ValueError("Lote no existente")
    
    if db_lote.codigo_de_lote != lote.codigo_de_lote and db.query(Lote).filter_by(codigo_de_lote=lote.codigo_de_lote).first():
        raise ValueError("El código del lote ya existe")

    producto = db.query(Producto).filter(Producto.codigo == lote.codigo_de_producto).first()
    if not producto:
        raise ValueError("Producto no existente")
        
    estado = db.query(EstadoDeLote).filter(EstadoDeLote.nombre == lote.estado_de_lote_nombre).first()
    if not estado:
        raise ValueError("Estado de lote no existente")
        
    ubicacion = db.query(Ubicacion).filter(Ubicacion.nombre == lote.ubicacion_nombre).first()
    if not ubicacion:
        ubicacion = create_ubicacion(db, UbicacionCreate(nombre=lote.ubicacion_nombre))
        
    try:
        db_lote.codigo_de_lote = lote.codigo_de_lote
        db_lote.existencia = lote.existencia
        db_lote.fecha_de_vencimiento = lote.fecha_de_vencimiento
        db_lote.producto = producto
        db_lote.estado = estado
        db_lote.ubicacion = ubicacion
        db.commit()
        db.refresh(db_lote)
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    return db_lote

def delete_lote(db: Session, lote_id: int) -> None:
    db_lote = read_lote_by_id(db, lote_id)
    if not db_lote:
        raise ValueError("Lote no existente")
    try:
        db.delete(db_lote)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e