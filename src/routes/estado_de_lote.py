from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.estado_de_lote import (
    create_estado_de_lote,
    read_estados_de_lote,
    read_estado_de_lote_by_id,
    update_estado_de_lote,
    delete_estado_de_lote,
)
from dependency import get_db
from schema.estado_de_lote import (
    EstadoDeLoteCreate,
    EstadoDeLoteRead,
    EstadoDeLoteUpdate,
)
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/estados_de_lote"

@router.post(_endpoint, response_model=EstadoDeLoteRead)
def create_estado_de_lote_endpoint(
    estado: EstadoDeLoteCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_estado_de_lote(db, estado)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=list[EstadoDeLoteRead])
def read_estados_de_lote_endpoint(db: Session = Depends(get_db)):
    try:
        return read_estados_de_lote(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener estados de lote")

@router.get(f"{_endpoint}/{{estado_id}}", response_model=EstadoDeLoteRead)
def read_estado_de_lote_endpoint(
    estado_id: int,
    db: Session = Depends(get_db)
):
    try:
        return read_estado_de_lote_by_id(db, estado_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Estado de lote no existente")

@router.put(f"{_endpoint}/{{estado_id}}", response_model=EstadoDeLoteRead)
def update_estado_de_lote_endpoint(
    estado_id: int,
    estado: EstadoDeLoteUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_estado_de_lote(db, estado_id, estado)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(f"{_endpoint}/{{estado_id}}", response_model=dict)
def delete_estado_de_lote_endpoint(
    estado_id: int,
    db: Session = Depends(get_db)
):
    try:
        delete_estado_de_lote(db, estado_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Estado de lote eliminada"}