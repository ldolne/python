from .base import Base, category_plant
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .plant import Plant

class Category(Base):
    __tablename__ = "category" # ou __name__, correct aussi
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    plants: Mapped[list["Plant"]] = relationship(secondary=category_plant, back_populates="categories")