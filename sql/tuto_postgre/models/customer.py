from models.plant import Plant

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .order import Order # pour éviter référence circulaire, ajouter un import comme type uniquement ; sert à l'autocomplétion et le typage

class Customer(Base): # model en Laravel
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column("last_name")
    first_name: Mapped[str] = mapped_column("first_name")
    orders: Mapped[list["Order"]] = relationship(back_populates='customer') # nom de la propriété inverse ; relation bidirectionnelle (pas obligatoire)

    def place_order(self, session, items: list[tuple[Plant, int]]):
        from .order import Order
        from .order_line import OrderLine
        from datetime import date 

        order = Order(
            order_date=date.today(),
            status=Order.Status.PENDING,
            customer=self # car on est déjà dans la classe ; le lien se fait via l'ID, quand le client sera créé
        )

        session.add(order)

        for plant, quantity in items:
            line = OrderLine(plant=plant, order=order, quantity=quantity, unit_price=plant.base_price)
            session.add(line)

        return order