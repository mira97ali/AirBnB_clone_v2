#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"

    name = sqlalchemy.Column(
        sqlalchemy.String(128),
        nullable=False)
    place_amenities = relationship(
        "Place",
        secondary=place_amenity)
