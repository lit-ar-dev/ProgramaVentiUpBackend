from __future__ import annotations
from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class MedidaDeVenta(Base):
    __tablename__ = "medida_de_venta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )

    if TYPE_CHECKING:
        from models.unidad_de_medida import UnidadDeMedida

    unidades: Mapped[List[UnidadDeMedida]] = relationship(
        "UnidadDeMedida", back_populates="medida_de_venta"
    )