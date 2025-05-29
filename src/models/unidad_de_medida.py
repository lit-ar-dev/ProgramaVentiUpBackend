from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class UnidadDeMedida(Base):
    __tablename__ = "unidad_de_medida"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    if TYPE_CHECKING:
        from models.medida_de_venta import MedidaDeVenta
        from models.producto import Producto

    medida_de_venta_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("medida_de_venta.id"), nullable=False
    )
    medida_de_venta: Mapped[MedidaDeVenta] = relationship(
        "MedidaDeVenta", back_populates="unidades"
    )

    productos: Mapped[List[Producto]] = relationship(
        "Producto", back_populates="unidad_de_medida"
    )

    @property
    def medida_de_venta_nombre(self) -> Optional[str]:
        return self.medida_de_venta.nombre if self.medida_de_venta else None