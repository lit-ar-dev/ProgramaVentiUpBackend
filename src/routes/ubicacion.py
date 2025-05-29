from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.ubicacion import (
    create_ubicacion,
    read_ubicaciones,
    read_ubicacion_by_id,
    update_ubicacion,
    delete_ubicacion,
)
from dependency import get_db
from schema.ubicacion import (
    UbicacionCreate,
    UbicacionRead,
    UbicacionUpdate,
)
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/ubicaciones"

@router.post(_endpoint, response_model=UbicacionRead)
def create_ubicacion_endpoint(
    ubicacion: UbicacionCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_ubicacion(db, ubicacion)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=list[UbicacionRead])
def read_ubicaciones_endpoint(db: Session = Depends(get_db)):
    try:
        return read_ubicaciones(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener ubicaciones")

@router.get(f"{_endpoint}/{{ubicacion_id}}", response_model=UbicacionRead)
def read_ubicacion_endpoint(
    ubicacion_id: int,
    db: Session = Depends(get_db)
):
    try:
        return read_ubicacion_by_id(db, ubicacion_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Ubicación no existente")

@router.put(f"{_endpoint}/{{ubicacion_id}}", response_model=UbicacionRead)
def update_ubicacion_endpoint(
    ubicacion_id: int,
    ubicacion: UbicacionUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_ubicacion(db, ubicacion_id, ubicacion)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(f"{_endpoint}/{{ubicacion_id}}", response_model=dict)
def delete_ubicacion_endpoint(
    ubicacion_id: int,
    db: Session = Depends(get_db)
):
    try:
        delete_ubicacion(db, ubicacion_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Ubicación eliminada"}