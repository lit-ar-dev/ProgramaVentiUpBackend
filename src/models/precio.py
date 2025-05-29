from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING, Optional
from sqlalchemy import Integer, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Precio(Base):
    __tablename__ = "precio"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    fecha_de_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_de_fin: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    if TYPE_CHECKING:
        from models.producto import Producto

    producto_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("producto.id"), nullable=False
    )
    producto: Mapped[Producto] = relationship("Producto", back_populates="precios")

    @property
    def codigo_de_producto(self) -> Optional[str]:
        return self.producto.codigo if self.producto else None