from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud.venta import (
    delete_venta,
    read_ventas,
    read_venta_by_id,
    create_venta
)
from dependency import get_db
from schema.venta import VentaCreate, VentaRead, VentaUpdate
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/ventas"

@router.post(_endpoint, response_model=VentaRead)
def create_venta_endpoint(venta: VentaCreate, db: Session = Depends(get_db)):
    try:
        return create_venta(
            db,
            venta
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=List[VentaRead])
def read_ventas_endpoint(db: Session = Depends(get_db)):
    try:
        return read_ventas(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener ventas")

@router.get(f"{_endpoint}/{{venta_id}}", response_model=VentaRead)
def read_venta_endpoint(venta_id: int, db: Session = Depends(get_db)):
    try:
        return read_venta_by_id(db, venta_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Venta no existente")

@router.put(f"{_endpoint}/{{venta_id}}", response_model=VentaRead)
def update_venta_endpoint(
    venta_id: int,
    venta: VentaUpdate,
    db: Session = Depends(get_db)
):
    pass

@router.delete(f"{_endpoint}/{{venta_id}}")
def delete_venta_endpoint(
    venta_id: int,
    db: Session = Depends(get_db)
):
    try:
        delete_venta(db, venta_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Venta eliminada"}
