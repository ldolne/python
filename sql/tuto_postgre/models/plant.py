from decimal import Decimal

from sqlalchemy import String, DECIMAL

from .base import Base
from .relations import category_plant
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .order_line import OrderLine
    from .stock import Stock
    from .category import Category

class Plant(Base):
    __tablename__ = "plant"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True) # définit la longueur de la str en db
    description: Mapped[str] = mapped_column(nullable=True)
    base_price: Mapped[Decimal] = mapped_column(DECIMAL(6,2)) # decimal a virgule fixe

    stocks: Mapped[list["Stock"]] = relationship(back_populates='plant')
    order_lines: Mapped[list["OrderLine"]] = relationship(back_populates='plant')
    categories: Mapped[list["Category"]] = relationship(secondary=category_plant, back_populates="plants") # "category_plant", le nom de la table, est suffisant, car la table sera créée