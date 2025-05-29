from __future__ import annotations
from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base

class Marca(Base):
    __tablename__ = "marca"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )

    if TYPE_CHECKING:
        from models.producto import Producto

    productos: Mapped[List[Producto]] = relationship("Producto", back_populates="marca")