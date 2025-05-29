from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from crud.marca import create_marca, read_marca_by_nombre
from crud.unidad_de_medida import read_unidad_de_medida_by_nombre
from models.precio import Precio
from models.producto import Producto
from schema.marca import MarcaCreate
from schema.producto import ProductoCreate, ProductoUpdate


def create_producto(
    db: Session,
    producto: ProductoCreate
) -> Producto:
    if read_producto_by_codigo(db, producto.codigo):
        raise ValueError("El código del producto ya existe")
        
    marca = read_marca_by_nombre(db, producto.marca_nombre)
    unidad_de_medida = read_unidad_de_medida_by_nombre(db, producto.unidad_de_medida_nombre)

    if not unidad_de_medida:
        raise ValueError("Unidad de medida no existente")
        
    if not marca:
        marca = create_marca(db, MarcaCreate(nombre=producto.marca_nombre))
        
    if producto.precio <= 0:
        raise ValueError("El precio debe ser mayor que cero")

    try:
        db_producto = Producto(
            codigo=producto.codigo,
            nombre=producto.nombre,
            descripcion=producto.descripcion,
            marca=marca,
            unidad_de_medida=unidad_de_medida
        )
        db.add(db_producto)
        db.commit()

        db_precio = Precio(precio=producto.precio, fecha_de_inicio=date.today(), producto=db_producto)
        db.add(db_precio)
        db.commit()
        db.refresh(db_producto)

        return db_producto
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise e

def read_productos(db: Session):
    return db.query(Producto).all()

def read_producto_by_id(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()
    
def read_producto_by_codigo(db: Session, codigo: str):
    return db.query(Producto).filter(Producto.codigo == codigo).first()
    
def update_producto(
    db: Session,
    producto_id: int,
    producto: ProductoUpdate
) -> Producto:
    db_producto = read_producto_by_id(db, producto_id)
    if not db_producto:
        raise ValueError("Producto no existente")

    if db_producto.codigo != producto.codigo and read_producto_by_codigo(db, producto.codigo):
        raise ValueError("El código del producto ya existe")

    marca = read_marca_by_nombre(db, producto.marca_nombre)
    if not marca:
        marca = create_marca(db, MarcaCreate(nombre=producto.marca_nombre))

    unidad = read_unidad_de_medida_by_nombre(db, producto.unidad_de_medida_nombre)
    if not unidad:
        raise ValueError("Unidad de medida no existente")

    if producto.precio <= 0:
        raise ValueError("El precio debe ser mayor que cero")

    try:
        db_producto.codigo = producto.codigo
        db_producto.nombre = producto.nombre
        db_producto.descripcion = producto.descripcion
        db_producto.marca = marca
        db_producto.unidad_de_medida = unidad
        db.commit()

        ultimo_precio = db.query(Precio).filter(Precio.producto_id == producto_id) \
            .order_by(Precio.fecha_de_inicio.desc()).first()
        if not ultimo_precio or ultimo_precio.precio != producto.precio:
            if ultimo_precio:
                ultimo_precio.fecha_de_fin = date.today()
                db.add(ultimo_precio)
                db.commit()

            db_precio = Precio(precio=producto.precio, fecha_de_inicio=date.today(), producto=db_producto)
            db.add(db_precio)
            db.commit()

        db.refresh(db_producto)
        return db_producto
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise e

def delete_producto(db: Session, producto_id: int) -> None:
    db_producto = read_producto_by_id(db, producto_id)
    if not db_producto:
        raise ValueError("Producto no existente")
    try:
        db.delete(db_producto)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e