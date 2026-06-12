# Associative tables
from sqlalchemy import Column, ForeignKey, Table

from models.base import Base


category_plant = Table(
    "category_plant",
    Base.metadata,
    Column("category_id", ForeignKey("category.id")),
    Column("plant_id", ForeignKey("plant.id")),
)