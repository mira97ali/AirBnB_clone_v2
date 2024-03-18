#!/usr/bin/python3
""" City Module for HBNB project """
import sqlalchemy
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = sqlalchemy.Column(
        sqlalchemy.String(128),
        nullable=False)
    state_id = sqlalchemy.Column(
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey("states.id"),
        nullable=False)
    places = relationship(
        "Place",
        cascade="all, delete, delete-orphan",
        backref="cities")
