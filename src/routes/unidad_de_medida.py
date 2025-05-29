from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.unidad_de_medida import create_unidad_de_medida, read_unidad_de_medida_by_id, read_unidades_de_medida
from dependency import get_db
from schema.unidad_de_medida import UnidadDeMedidaCreate, UnidadDeMedidaRead
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/unidades_de_medida"

@router.post(_endpoint, response_model=UnidadDeMedidaRead)
def create_unidad_de_medida_endpoint(unidad_de_medida: UnidadDeMedidaCreate, db: Session = Depends(get_db)):
    try:
        return create_unidad_de_medida(db, unidad_de_medida)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=list[UnidadDeMedidaRead])
def read_unidades_de_medida_endpoint(db: Session = Depends(get_db)):
    try:
        return read_unidades_de_medida(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener unidades de medida")

@router.get(f"{_endpoint}/{{unidad_de_medida_id}}", response_model=UnidadDeMedidaRead)
def read_unidad_de_medida_endpoint(unidad_de_medida_id: int, db: Session = Depends(get_db)):
    try:
        return read_unidad_de_medida_by_id(db, unidad_de_medida_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Unidad de medida no existente")