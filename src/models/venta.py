from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Venta(Base):
    __tablename__ = "venta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    importe_total: Mapped[float] = mapped_column(Float, nullable=False)

    if TYPE_CHECKING:
        from models.detalle_de_venta import DetalleDeVenta
        from models.cliente import Cliente
        from models.usuario import Usuario
        from models.metodo_de_pago import MetodoDePago

    metodo_de_pago_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("metodo_de_pago.id"), nullable=False
    )
    cliente_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("cliente.id"), nullable=False
    )
    cajero_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("usuario.id"), nullable=False
    )

    metodo_de_pago: Mapped[MetodoDePago] = relationship(
        "MetodoDePago", back_populates="ventas"
    )
    cliente: Mapped[Cliente] = relationship(
        "Cliente", back_populates="ventas"
    )
    cajero: Mapped[Usuario] = relationship(
        "Usuario", back_populates="ventas"
    )
    detalles: Mapped[List[DetalleDeVenta]] = relationship(
        "DetalleDeVenta", back_populates="venta", cascade="all, delete-orphan"
    )