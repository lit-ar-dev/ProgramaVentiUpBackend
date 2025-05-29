from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from crud.cliente import create_cliente, read_cliente_by_nombre
from crud.detalle_de_venta import create_detalle_de_venta
from crud.metodo_de_pago import read_metodo_de_pago_by_nombre
from crud.usuario import create_usuario, read_usuario_by_nombre
from models.venta import Venta
from schema.cliente import ClienteCreate
from schema.usuario import UsuarioCreate
from schema.venta import VentaCreate


def create_venta(
    db: Session,
    venta: VentaCreate
) -> Venta:
    metodo_de_pago = read_metodo_de_pago_by_nombre(db, venta.metodo_de_pago_nombre)
    if not metodo_de_pago:
        raise ValueError("Método de pago no existente")

    cliente = read_cliente_by_nombre(db, venta.cliente_nombre)
    if not cliente:
        cliente = create_cliente(db, ClienteCreate(nombre=venta.cliente_nombre))
        
    cajero = read_usuario_by_nombre(db, venta.cajero_nombre)
    if not cajero:
        cajero = create_usuario(db, UsuarioCreate(nombre=venta.cajero_nombre))
        
    if venta.importe_total <= 0:
        raise ValueError("El importe total debe ser mayor que cero")
    
    try:
        db_venta = Venta(
            fecha=venta.fecha,
            metodo_de_pago=metodo_de_pago,
            cliente=cliente,
            cajero=cajero,
            importe_total=venta.importe_total,
        )
        db.add(db_venta)
        db.commit()
        db.refresh(db_venta)

        for detalle_de_venta in venta.detalle:
            nuevo_detalle_de_venta = create_detalle_de_venta(
                db,
                detalle_de_venta=detalle_de_venta,
                nueva_venta=db_venta,
            )
            db_venta.detalles.append(nuevo_detalle_de_venta)
        return db_venta
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def read_ventas(db: Session):
    return db.query(Venta).all()

def read_venta_by_id(db: Session, venta_id: int):
    return db.query(Venta).filter(Venta.id == venta_id).first()

def delete_venta(db: Session, venta_id: int) -> None:
    db_venta = read_venta_by_id(db, venta_id)
    if not db_venta:
        raise ValueError("Venta no existente")
    try:
        db.delete(db_venta)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e