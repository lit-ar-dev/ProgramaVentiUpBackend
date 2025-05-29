from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class DetalleDeVenta(Base):
    __tablename__ = "detalle_de_venta"

    renglon: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    cantidad: Mapped[float] = mapped_column(Float, nullable=False)

    venta_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("venta.id"), nullable=False
    )
    producto_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("producto.id"), nullable=False
    )
    lote_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("lote.id"), nullable=False
    )

    if TYPE_CHECKING:
        from models.venta import Venta
        from models.producto import Producto
        from models.lote import Lote

    venta: Mapped[Venta] = relationship("Venta", back_populates="detalles")
    producto: Mapped[Producto] = relationship(
        "Producto", back_populates="detalles_de_venta"
    )
    lote: Mapped[Lote] = relationship("Lote", back_populates="detalles_de_venta")