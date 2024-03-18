#!/usr/bin/python3
""" Place Module for HBNB project """
import sqlalchemy

from models.base_model import BaseModel, Base


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
