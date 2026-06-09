from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase

class Base(MappedAsDataclass, DeclarativeBase):
    pass

# Associative tables
category_plant = Table(
    "category_plant",
    Base.metadata,
    Column("category_id", ForeignKey("category.id")),
    Column("plant_id", ForeignKey("plant.id")),
)