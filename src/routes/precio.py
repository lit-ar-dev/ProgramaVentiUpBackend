from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud.precio import (
    create_precio,
    read_precios,
    read_precio_by_id,
    update_precio,
    delete_precio
)
from schema.precio import PrecioCreate, PrecioRead, PrecioUpdate
from dependency import get_db
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/precios"

@router.post(_endpoint, response_model=PrecioRead)
def create_precio_endpoint(precio: PrecioCreate, db: Session = Depends(get_db)):
    try:
        return create_precio(
            db,
            precio
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=List[PrecioRead])
def read_precios_endpoint(db: Session = Depends(get_db)):
    try:
        return read_precios(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener precios")

@router.get(f"{_endpoint}/{{precio_id}}", response_model=PrecioRead)
def read_precio_endpoint(precio_id: int, db: Session = Depends(get_db)):
    try:
        return read_precio_by_id(db, precio_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Precio no existente")

@router.put(f"{_endpoint}/{{precio_id}}", response_model=PrecioRead)
def update_precio_endpoint(precio_id: int, precio: PrecioUpdate, db: Session = Depends(get_db)):
    try:
        return update_precio(
            db,
            precio_id,
            precio
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(f"{_endpoint}/{{precio_id}}")
def delete_precio_endpoint(precio_id: int, db: Session = Depends(get_db)):
    try:
        delete_precio(db, precio_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Precio eliminado"}
