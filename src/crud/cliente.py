from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.cliente import Cliente
from schema.cliente import ClienteCreate, ClienteUpdate


def create_cliente(db: Session, cliente_create: ClienteCreate) -> Cliente:
    try:
        db_cliente = Cliente(nombre=cliente_create.nombre, numero_de_telefono=cliente_create.numero_de_telefono)
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
def read_clientes(db: Session):
    return db.query(Cliente).all()

def read_cliente_by_id(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def read_cliente_by_nombre(db: Session, nombre: str):
    return db.query(Cliente).filter(Cliente.nombre == nombre).first()

def update_cliente(db: Session, cliente_id: int, cliente: ClienteUpdate) -> Cliente:
    db_cliente = read_cliente_by_id(db, cliente_id)
    if not db_cliente:
        raise ValueError("Cliente no existente")
    try:
        db_cliente.nombre = cliente.nombre
        db_cliente.numero_de_telefono = cliente.numero_de_telefono
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def delete_cliente(db: Session, cliente_id: int) -> None:
    db_cliente = read_cliente_by_id(db, cliente_id)
    if not db_cliente:
        raise ValueError("Cliente no existente")
    try:
        db.delete(db_cliente)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e