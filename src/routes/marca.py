from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.marca import create_marca, delete_marca, read_marca_by_id, read_marcas, update_marca
from dependency import get_db
from schema.marca import MarcaCreate, MarcaRead, MarcaUpdate
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()
_endpoint = "/marcas"

@router.post(_endpoint, response_model=MarcaRead)
def create_marca_endpoint(marca: MarcaCreate, db: Session = Depends(get_db)):
    try:
        return create_marca(db, marca)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(_endpoint, response_model=list[MarcaRead])
def read_marcas_endpoint(db: Session = Depends(get_db)):
    try:
        return read_marcas(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener marcas")

@router.get(f"{_endpoint}/{{marca_id}}", response_model=MarcaRead)
def read_marca_endpoint(marca_id: int, db: Session = Depends(get_db)):
    try:
        return read_marca_by_id(db, marca_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=404, detail="Marca no existente")

@router.put(f"{_endpoint}/{{marca_id}}", response_model=MarcaRead)
def update_marca_endpoint(marca_id: int, marca: MarcaUpdate, db: Session = Depends(get_db)):
    try:
        return update_marca(db, marca_id, marca)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(f"{_endpoint}/{{marca_id}}", response_model=dict)
def delete_marca_endpoint(marca_id: int, db: Session = Depends(get_db)):
    try:
        delete_marca(db, marca_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Marca eliminada"}