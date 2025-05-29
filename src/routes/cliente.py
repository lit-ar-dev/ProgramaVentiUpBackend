from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud.cliente import (
    read_clientes,
    read_cliente_by_id,
    create_cliente,
    update_cliente,
    delete_cliente
)
from dependency import get_db
from schema.cliente import ClienteCreate, ClienteRead, ClienteUpdate
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/clientes"

@router.post(_endpoint, response_model=ClienteRead)
def create_cliente_endpoint(
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_cliente(db, cliente)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=List[ClienteRead])
def read_clientes_endpoint(db: Session = Depends(get_db)):
    try:
        return read_clientes(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener clientes")

@router.get(f"{_endpoint}/{"{cliente_id}"}", response_model=ClienteRead)
def read_cliente_endpoint(cliente_id: int, db: Session = Depends(get_db)):
    try:
        return read_cliente_by_id(db, cliente_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Cliente no existente")

@router.put(f"{_endpoint}/{"{cliente_id}"}", response_model=ClienteRead)
def update_cliente_endpoint(
    cliente_id: int,
    cliente: ClienteUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_cliente(db, cliente_id, cliente)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(f"{_endpoint}/{"{cliente_id}"}")
def delete_cliente_endpoint(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    try:
        delete_cliente(db, cliente_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Cliente eliminado correctamente"}