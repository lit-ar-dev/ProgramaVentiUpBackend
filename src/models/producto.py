from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Producto(Base):
    __tablename__ = "producto"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    codigo: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    if TYPE_CHECKING:
        from models.marca import Marca
        from models.unidad_de_medida import UnidadDeMedida
        from models.precio import Precio
        from models.lote import Lote
        from models.detalle_de_venta import DetalleDeVenta

    marca_id: Mapped[int] = mapped_column(Integer, ForeignKey("marca.id"), nullable=False)
    marca: Mapped[Marca] = relationship("Marca", back_populates="productos")

    unidad_de_medida_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("unidad_de_medida.id"), nullable=False
    )
    unidad_de_medida: Mapped[UnidadDeMedida] = relationship(
        "UnidadDeMedida", back_populates="productos"
    )

    precios: Mapped[List[Precio]] = relationship(
        "Precio",
        back_populates="producto",
        order_by="Precio.fecha_de_inicio.desc()",
        cascade="all, delete-orphan",
        lazy="select"
    )

    stock: Mapped[List[Lote]] = relationship(
        "Lote",
        back_populates="producto",
        order_by="Lote.fecha_de_vencimiento.desc()",
        cascade="all, delete-orphan",
        lazy="select"
    )

    detalles_de_venta: Mapped[List[DetalleDeVenta]] = relationship(
        "DetalleDeVenta",
        back_populates="producto",
        order_by="DetalleDeVenta.renglon.desc()",
        cascade="all, delete-orphan",
        lazy="select"
    )

    @property
    def precio(self) -> Optional[float]:
        return self.precios[0].precio if self.precios else None

    @property
    def medida_de_venta_nombre(self) -> Optional[str]:
        return (
            self.unidad_de_medida.medida_de_venta.nombre
            if self.unidad_de_medida and self.unidad_de_medida.medida_de_venta
            else None
        )

    @property
    def unidad_de_medida_nombre(self) -> Optional[str]:
        return self.unidad_de_medida.nombre if self.unidad_de_medida else None

    @property
    def marca_nombre(self) -> Optional[str]:
        return self.marca.nombre if self.marca else None