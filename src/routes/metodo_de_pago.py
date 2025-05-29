from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.metodo_de_pago import (
    create_metodo_de_pago,
    read_metodos_de_pago,
    read_metodo_de_pago_by_id,
    update_metodo_de_pago,
    delete_metodo_de_pago,
)
from dependency import get_db
from schema.metodo_de_pago import (
    MetodoDePagoCreate,
    MetodoDePagoRead,
    MetodoDePagoUpdate,
)
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/metodos_de_pago"

@router.post(_endpoint, response_model=MetodoDePagoRead)
def create_metodo_de_pago_endpoint(
    metodo_de_pago: MetodoDePagoCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_metodo_de_pago(db, metodo_de_pago)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=list[MetodoDePagoRead])
def read_metodos_de_pago_endpoint(db: Session = Depends(get_db)):
    try:
        return read_metodos_de_pago(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener métodos de pago")

@router.get(f"{_endpoint}/{{metodo_de_pago_id}}", response_model=MetodoDePagoRead)
def read_metodo_de_pago_endpoint(
    metodo_de_pago_id: int,
    db: Session = Depends(get_db)
):
    try:
        return read_metodo_de_pago_by_id(db, metodo_de_pago_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Método de pago no existente")

@router.put(f"{_endpoint}/{{metodo_de_pago_id}}", response_model=MetodoDePagoRead)
def update_metodo_de_pago_endpoint(
    metodo_de_pago_id: int,
    metodo_de_pago: MetodoDePagoUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_metodo_de_pago(db, metodo_de_pago_id, metodo_de_pago)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(f"{_endpoint}/{{metodo_de_pago_id}}", response_model=dict)
def delete_metodo_de_pago_endpoint(
    metodo_de_pago_id: int,
    db: Session = Depends(get_db)
):
    try:
        delete_metodo_de_pago(db, metodo_de_pago_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Método de pago eliminado"}