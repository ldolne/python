from enum import Enum

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as SQLEnum, ForeignKey
from datetime import date

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import OrderLine
    from models import Customer # pour éviter référence circulaire, ajouter un import comme type uniquement ; sert à l'autocomplétion et le typage, MAIS n'importe plus la classe

class Order(Base):
    class Status(Enum): # classe imbriquée
        PENDING = "PENDING"
        CREATED = "CREATED"
        CLOSED = "CLOSED"
        CANCELED = "CANCELED"

    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[date] = mapped_column()
    status: Mapped[Status] = mapped_column(SQLEnum(Status))
    # customer_id: Mapped[int] = mapped_column()
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped["Customer"] = relationship(back_populates='orders') # nom de la propriété inverse ; relation bidirectionnelle (pas obligatoire)
    order_lines: Mapped[list["OrderLine"]] = relationship(back_populates='order')

