from __future__ import annotations
from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class Ubicacion(Base):
    __tablename__ = "ubicacion"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True, index=True
    )

    if TYPE_CHECKING:
        from models.lote import Lote

    stock: Mapped[List[Lote]] = relationship("Lote", back_populates="ubicacion")