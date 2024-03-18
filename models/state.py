#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        backref="state")

    @property
    def cities(self):
        objects = models.storage.all()
        list_of_cities = []
        for obj in objects:
            instance_values = obj.replace(".", " ").split()
            instance = objects[obj]
            if instance_values[0] == "City" and instance.state_id == self.id:
                list_of_cities.append(instance)
        return list_of_cities
