from __future__ import annotations
from typing import TYPE_CHECKING, List
from datetime import date
from sqlalchemy import Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base
from models.producto import Producto
from models.estado_de_lote import EstadoDeLote
from models.ubicacion import Ubicacion
from models.detalle_de_venta import DetalleDeVenta


class Lote(Base):
    __tablename__ = "lote"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    codigo_de_lote: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    existencia: Mapped[float] = mapped_column(Float, nullable=False)
    fecha_de_vencimiento: Mapped[date] = mapped_column(Date, nullable=False)

    producto_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("producto.id"), nullable=False
    )
    estado_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("estado_de_lote.id"), nullable=False
    )
    ubicacion_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ubicacion.id"), nullable=False
    )

    if TYPE_CHECKING:
        from models.producto import Producto
        from models.estado_de_lote import EstadoDeLote
        from models.ubicacion import Ubicacion
        from models.detalle_de_venta import DetalleDeVenta

    producto: Mapped[Producto] = relationship("Producto", back_populates="stock")
    estado: Mapped[EstadoDeLote] = relationship("EstadoDeLote", back_populates="stock")
    ubicacion: Mapped[Ubicacion] = relationship("Ubicacion", back_populates="stock")
    detalles_de_venta: Mapped[List[DetalleDeVenta]] = relationship(
        "DetalleDeVenta", back_populates="lote"
    )

    @property
    def estado_de_lote_nombre(self) -> str:
        return self.estado.nombre

    @property
    def ubicacion_nombre(self) -> str:
        return self.ubicacion.nombre