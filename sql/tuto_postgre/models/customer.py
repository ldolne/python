from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .order import Order # pour éviter référence circulaire, ajouter un import comme type uniquement ; sert à l'autocomplétion et le typage

class Customer(Base): # model en Laravel
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column("last_name")
    first_name: Mapped[str] = mapped_column("first_name")
    orders: Mapped[list["Order"]] = relationship(back_populates='customer') # nom de la propriété inverse ; relation bidirectionnelle (pas obligatoire)
