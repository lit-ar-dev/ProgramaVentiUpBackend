from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.detalle_de_venta import DetalleDeVenta
from models.lote import Lote
from models.producto import Producto
from models.venta import Venta
from schema.detalle_de_venta import DetalleDeVentaCreate


def create_detalle_de_venta(
    db: Session,
    detalle_de_venta: DetalleDeVentaCreate,
    nueva_venta: Venta
) -> DetalleDeVenta:
    producto = db.query(Producto).filter(Producto.codigo == detalle_de_venta.codigo_de_producto).first()
    if not producto:
        raise ValueError("Producto no existente")
    
    lote = db.query(Lote).filter(Lote.codigo_de_lote == detalle_de_venta.codigo_de_lote).first()
    if not lote:
        raise ValueError("Lote no existente")
    
    if detalle_de_venta.cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")
    
    if detalle_de_venta.precio <= 0:
        raise ValueError("El precio debe ser mayor que cero")

    try:
        nuevo_detalle = DetalleDeVenta(
            precio=detalle_de_venta.precio,
            cantidad=detalle_de_venta.cantidad,
            venta=nueva_venta,
            producto=producto,
            lote=lote,
        )
        db.add(nuevo_detalle)
        db.commit()
        db.refresh(nuevo_detalle)

        # Actualizar el stock del producto
        lote.existencia -= detalle_de_venta.cantidad
        if lote.existencia < 0:
            raise ValueError("No hay suficiente stock en el lote")
        db.commit()
        db.refresh(lote)

        return nuevo_detalle
    except SQLAlchemyError as e:
        db.rollback()
        raise e