from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.lote import (
    create_lote,
    read_lotes,
    read_lote_by_id,
    update_lote,
    delete_lote,
)
from dependency import get_db
from schema.lote import LoteCreate, LoteRead, LoteUpdate
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()
_endpoint = "/stock"

@router.post(_endpoint, response_model=LoteRead)
def create_lote_endpoint(
    lote: LoteCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_lote(
            db,
            lote
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=list[LoteRead])
def read_lotes_endpoint(db: Session = Depends(get_db)):
    try:
        return read_lotes(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener lotes")

@router.get(f"{_endpoint}/{{lote_id}}", response_model=LoteRead)
def read_lote_endpoint(
    lote_id: int,
    db: Session = Depends(get_db)
):
    try:
        return read_lote_by_id(db, lote_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Lote no existente")

@router.put(f"{_endpoint}/{{lote_id}}", response_model=LoteRead)
def update_lote_endpoint(
    lote_id: int,
    lote: LoteUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_lote(
            db,
            lote_id,
            lote
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(f"{_endpoint}/{{lote_id}}", response_model=dict)
def delete_lote_endpoint(
    lote_id: int,
    db: Session = Depends(get_db)
):
    try:
        delete_lote(db, lote_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Lote eliminado"}
