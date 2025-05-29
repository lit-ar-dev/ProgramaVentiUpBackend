from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Cliente(Base):
    __tablename__ = "cliente"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    numero_de_telefono: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)

    if TYPE_CHECKING:
        from models.venta import Venta

    ventas: Mapped[List[Venta]] = relationship("Venta", back_populates="cliente")