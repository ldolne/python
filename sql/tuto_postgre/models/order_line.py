from decimal import Decimal

from .base import Base
from .plant import Plant
from .order import Order
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DECIMAL, ForeignKey

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .order import Order
    from .plant import Plant

class OrderLine(Base):
    __tablename__ = "order_line"
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), primary_key=True) # composite key
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column()
    unit_price: Mapped[Decimal] = mapped_column(DECIMAL(6,2))

    order: Mapped["Order"] = relationship(back_populates='order_lines')
    plant: Mapped["Plant"] = relationship(back_populates='order_lines')