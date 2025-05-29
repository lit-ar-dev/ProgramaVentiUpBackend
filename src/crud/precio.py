from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from crud.producto import read_producto_by_codigo
from models.precio import Precio
from datetime import date
from models.producto import Producto
from schema.precio import PrecioCreate, PrecioUpdate


def create_precio(db: Session, precio: PrecioCreate) -> Precio:
    producto = db.query(Producto).filter(Producto.codigo == precio.codigo_de_producto).first()
    if not producto:
        raise ValueError("Producto no existente")
    
    db_precio = Precio(
        precio=precio.precio,
        fecha_de_inicio=precio.fecha_de_inicio,
        fecha_de_fin=precio.fecha_de_fin,
        producto=producto,
    )
    try:
        ultimo_precio = db.query(Precio).filter(
            Precio.producto_id == producto.id,
            Precio.fecha_de_fin == None
        )
        ultimo_precio.update({"fecha_de_fin": precio.fecha_de_inicio})
        db.commit()
        db.add(db_precio)
        db.commit()
        db.refresh(db_precio)

        return db_precio
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def read_precios(db: Session):
    return db.query(Precio).all()

def read_precio_by_id(db: Session, precio_id: int):
    return db.query(Precio).filter(Precio.id == precio_id).first()

def update_precio(db: Session, precio_id: int, precio: PrecioUpdate) -> Precio:
    db_precio = read_precio_by_id(db, precio_id)
    if not db_precio:
        raise ValueError("Precio no existente")
    
    producto = read_producto_by_codigo(db, precio.codigo_de_producto)
    if not producto:
        raise ValueError("Producto no existente")

    try:
        db_precio.precio = precio.precio
        db_precio.fecha_de_inicio = precio.fecha_de_inicio
        db_precio.fecha_de_fin = precio.fecha_de_fin
        db_precio.producto = producto

        db.commit()
        db.refresh(db_precio)
        return db_precio
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def delete_precio(db: Session, precio_id: int):
    db_precio = read_precio_by_id(db, precio_id)
    if not db_precio:
        raise ValueError("Precio no existente")

    try:
        db.delete(db_precio)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e