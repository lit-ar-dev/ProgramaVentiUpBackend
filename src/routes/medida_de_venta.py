from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.medida_de_venta import create_medida_de_venta, read_medida_de_venta, read_medidas_de_venta
from dependency import get_db
from schema.medida_de_venta import MedidaDeVentaCreate, MedidaDeVentaRead
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/medidas_de_venta"

@router.post(_endpoint, response_model=MedidaDeVentaRead)
def create_medida_de_venta_endpoint(medida_de_venta: MedidaDeVentaCreate, db: Session = Depends(get_db)):
    try:
        return create_medida_de_venta(db, medida_de_venta)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=list[MedidaDeVentaRead])
def read_medidas_de_venta_endpoint(db: Session = Depends(get_db)):
    try:
        return read_medidas_de_venta(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener medidas de venta")

@router.get(f"{_endpoint}/{{medida_de_venta_id}}", response_model=MedidaDeVentaRead)
def read_medida_de_venta_endpoint(medida_de_venta_id: int, db: Session = Depends(get_db)):
    try:
        return read_medida_de_venta(db, medida_de_venta_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Medida de venta no existente")