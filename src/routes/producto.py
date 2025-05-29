from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud.producto import (
    delete_producto,
    read_productos,
    read_producto_by_id,
    read_producto_by_codigo,
    create_producto,
    update_producto
)
from dependency import get_db
from schema.producto import ProductoCreate, ProductoRead, ProductoUpdate
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/productos"

@router.post(_endpoint, response_model=ProductoRead)
def create_producto_endpoint(producto: ProductoCreate, db: Session = Depends(get_db)):
    try:
        return create_producto(
            db,
            producto
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=List[ProductoRead])
def read_productos_endpoint(db: Session = Depends(get_db)):
    try:
        return read_productos(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener productos")

@router.get(f"{_endpoint}/{{producto_id}}", response_model=ProductoRead)
def read_producto_endpoint(producto_id: int, db: Session = Depends(get_db)):
    try:
        return read_producto_by_id(db, producto_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Producto no existente")

@router.get(f"{_endpoint}/codigo/{{codigo}}", response_model=ProductoRead)
def read_producto_by_codigo_endpoint(codigo: str, db: Session = Depends(get_db)):
    try:
        return read_producto_by_codigo(db, codigo)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Producto no existente")

@router.put(f"{_endpoint}/{{producto_id}}", response_model=ProductoRead)
def update_producto_endpoint(
    producto_id: int,
    producto: ProductoUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_producto(
            db,
            producto_id,
            producto
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(f"{_endpoint}/{{producto_id}}")
def delete_producto_endpoint(
    producto_id: int,
    db: Session = Depends(get_db)
):
    try:
        delete_producto(db, producto_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Producto eliminado correctamente"}
