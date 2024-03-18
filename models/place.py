#!/usr/bin/python3
""" Place Module for HBNB project """
import os

import sqlalchemy
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base


place_amenity = sqlalchemy.Table(
    "place_amenity",
    Base.metadata,
    sqlalchemy.Column(
        "place_id",
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    sqlalchemy.Column(
        "amenity_id",
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    amenity_ids = []

    city_id = sqlalchemy.Column(
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey("cities.id"),
        nullable=False)
    user_id = sqlalchemy.Column(
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey("users.id"),
        nullable=False)
    name = sqlalchemy.Column(
        sqlalchemy.String(128),
        nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String(1024))
    number_rooms = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
        default=0)
    number_bathrooms = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
        default=0)
    max_guest = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
        default=0)
    price_by_night = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
        default=0)
    latitude = sqlalchemy.Column(sqlalchemy.Float)
    longitude = sqlalchemy.Column(sqlalchemy.Float)

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review",
            cascade="all, delete, delete-orphan",
            backref="place")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            objects = models.storage.all()
            list_of_reviews = []
            for obj in objects:
                review = obj.replace(".", " ").split()
                instance = objects[obj]
                if review[0] == "Review" and instance.place_id == self.id:
                    list_of_reviews.append(instance)
            return list_of_reviews

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if "Amenity" in str(type(obj)) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
